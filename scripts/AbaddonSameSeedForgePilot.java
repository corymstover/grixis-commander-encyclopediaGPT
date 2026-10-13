package grixis.testing;

import forge.deck.Deck;
import forge.deck.io.DeckSerializer;
import forge.game.GameRules;
import forge.game.GameType;
import forge.game.Match;
import forge.game.player.RegisteredPlayer;
import forge.model.FModel;
import forge.player.GamePlayerUtil;
import forge.util.MyRandom;
import forge.view.SimulateMatch;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.EnumSet;
import java.util.List;
import java.util.Random;

/**
 * Runs same-seed exploratory Commander games in one initialized Forge JVM.
 *
 * This is a rules-engine/AI pilot, not a claim of real-world deck win rate.
 * The target baseline and variant are run separately against the same fixed
 * opponent using the same numeric RNG seeds. Forge Deck/CardPool normalization
 * uses unordered pools, so this does NOT guarantee matched opening hands or
 * matched initial libraries. Treat results as descriptive, unpaired AI observations.
 */
public final class AbaddonSameSeedForgePilot {
    private static final String FORGE_RELEASE = "forge-2.0.15";
    private static final String FORGE_COMMIT = "4ec5f1a2c32fa90ecb983a72b9eb47aa5c5d7676";
    private static final String BASELINE_LABEL = "Abaddon frozen baseline";
    private static final String VARIANT_LABEL = "Abaddon Aurora Phoenix test variant";
    private static final String OPPONENT_LABEL = "Ruthless Regiment fixed opponent";

    private AbaddonSameSeedForgePilot() {}

    public static void main(String[] args) throws Exception {
        Arguments options = Arguments.parse(args);
        Files.createDirectories(options.outputDir);
        FModel.initialize(null, null);

        Deck baseline = loadDeck(options.baseline);
        Deck variant = loadDeck(options.variant);
        Deck opponent = loadDeck(options.opponent);

        List<String> manifestLines = new ArrayList<>();
        manifestLines.add("trial_index,seed,baseline_log,variant_log,opponent_label,baseline_sha256,variant_sha256,opponent_sha256");
        String baselineHash = sha256(options.baseline);
        String variantHash = sha256(options.variant);
        String opponentHash = sha256(options.opponent);

        for (int pair = 0; pair < options.pairs; pair++) {
            long seed = options.baseSeed + pair;
            String baselineName = "Ai(1)-" + BASELINE_LABEL;
            String variantName = "Ai(1)-" + VARIANT_LABEL;
            String opponentName = "Ai(2)-" + OPPONENT_LABEL;

            String baselineLog = playOne(baseline, opponent, baselineName, opponentName, seed, options.timeoutSeconds);
            String variantLog = playOne(variant, opponent, variantName, opponentName, seed, options.timeoutSeconds);

            String baselineFile = String.format("seed-%d-baseline.log", seed);
            String variantFile = String.format("seed-%d-variant.log", seed);
            Files.writeString(options.outputDir.resolve(baselineFile), baselineLog, StandardCharsets.UTF_8);
            Files.writeString(options.outputDir.resolve(variantFile), variantLog, StandardCharsets.UTF_8);

            if (!baselineLog.contains("Game Result: Game 1 ended")) {
                throw new IllegalStateException("Baseline log lacks a completed result for seed " + seed);
            }
            if (!variantLog.contains("Game Result: Game 1 ended")) {
                throw new IllegalStateException("Variant log lacks a completed result for seed " + seed);
            }

            manifestLines.add(String.join(",",
                Integer.toString(pair + 1),
                Long.toString(seed),
                baselineFile,
                variantFile,
                csv(OPPONENT_LABEL),
                baselineHash,
                variantHash,
                opponentHash
            ));
            System.out.printf("SAME-SEED TRIAL %d/%d seed=%d baseline_result=%s variant_result=%s%n",
                pair + 1, options.pairs, seed, shortResult(baselineLog, baselineName), shortResult(variantLog, variantName));
        }

        Files.write(options.outputDir.resolve("same-seed-run-manifest.csv"),
            manifestLines, StandardCharsets.UTF_8);

        String manifest = "{\n"
            + "  \"forge_release\": \"" + FORGE_RELEASE + "\",\n"
            + "  \"forge_source_commit\": \"" + FORGE_COMMIT + "\",\n"
            + "  \"purpose\": \"same-seed but unpaired exploratory AI pilot; not a real-world win-rate estimate\",\n"
            + "  \"trials_per_list\": " + options.pairs + ",\n"
            + "  \"base_seed\": " + options.baseSeed + ",\n"
            + "  \"timeout_seconds_per_game\": " + options.timeoutSeconds + ",\n"
            + "  \"baseline_sha256\": \"" + baselineHash + "\",\n"
            + "  \"variant_sha256\": \"" + variantHash + "\",\n"
            + "  \"opponent_sha256\": \"" + opponentHash + "\",\n"
            + "  \"opponent\": \"" + OPPONENT_LABEL + "\",\n"
            + "  \"same_numeric_seed_values_used_for_each_trial\": true,\n"
            + "  \"same_seat_order\": true,\n"
            + "  \"starting_hand_pairing\": \"NOT GUARANTEED: Forge Deck/CardPool normalization uses unordered ItemPool iteration; equal seeds do not ensure identical opening hands or library order.\",\n"
            + "  \"limitations\": [\n"
            + "    \"Forge AI has known limitations on combo decks; all outcomes are conditional on this AI and this one fixed opponent.\",\n"
            + "    \"Forge DCK/CardPool iteration does not establish identical starting library order; treat each run as unpaired.\",\n"
            + "    \"This pilot tests log instrumentation and exploratory AI behavior only; it must not be used to choose the card slot.\",\n"
            + "    \"Raw per-game logs are preserved for event-level inspection.\"\n"
            + "  ]\n"
            + "}\n";
        Files.writeString(options.outputDir.resolve("pilot-manifest.json"), manifest, StandardCharsets.UTF_8);
        System.out.println("Wrote pilot artifacts to " + options.outputDir.toAbsolutePath());
    }

    private static Deck loadDeck(Path path) throws IOException {
        Deck deck = DeckSerializer.fromFile(path.toFile());
        if (deck == null) {
            throw new IOException("Forge could not load deck file: " + path);
        }
        return deck;
    }

    private static String playOne(Deck targetDeck, Deck opponentDeck, String targetName,
                                  String opponentName, long seed, int timeoutSeconds) throws Exception {
        ByteArrayOutputStream outputBytes = new ByteArrayOutputStream();
        ByteArrayOutputStream errorBytes = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        PrintStream originalErr = System.err;

        try (PrintStream capturedOut = new PrintStream(outputBytes, true, StandardCharsets.UTF_8);
             PrintStream capturedErr = new PrintStream(errorBytes, true, StandardCharsets.UTF_8)) {
            System.setOut(capturedOut);
            System.setErr(capturedErr);

            MyRandom.setRandom(new Random(seed));
            GameRules rules = new GameRules(GameType.Commander);
            rules.setAppliedVariants(EnumSet.of(GameType.Commander));
            rules.setSimTimeout(timeoutSeconds);

            List<RegisteredPlayer> players = new ArrayList<>();
            RegisteredPlayer target = RegisteredPlayer.forCommander(targetDeck);
            target.setPlayer(GamePlayerUtil.createAiPlayer(targetName, 0, ""));
            players.add(target);

            RegisteredPlayer opponent = RegisteredPlayer.forCommander(opponentDeck);
            opponent.setPlayer(GamePlayerUtil.createAiPlayer(opponentName, 1, ""));
            players.add(opponent);

            Match match = new Match(rules, players, "Abaddon Paired Pilot seed " + seed);
            SimulateMatch.simulateSingleMatch(match, 0, true);
        } finally {
            System.setOut(originalOut);
            System.setErr(originalErr);
        }

        String stdout = outputBytes.toString(StandardCharsets.UTF_8);
        String stderr = errorBytes.toString(StandardCharsets.UTF_8);
        if (!stderr.isBlank()) {
            stdout += "\n[HARNESS_CAPTURED_STDERR]\n" + stderr;
        }
        return stdout;
    }

    private static String shortResult(String log, String targetName) {
        for (String line : log.split("\\R")) {
            if (line.contains("Game Result: Game 1 ended")) {
                if (line.contains("a Draw")) {
                    return "DRAW";
                }
                return line.contains(targetName + " has won") ? "TARGET_WIN" :
                    line.toLowerCase().contains("has won") ? "OPPONENT_WIN" : "UNKNOWN";
            }
        }
        return "NO_RESULT";
    }

    private static String sha256(Path path) throws IOException, NoSuchAlgorithmException {
        byte[] data = Files.readAllBytes(path);
        byte[] digest = MessageDigest.getInstance("SHA-256").digest(data);
        StringBuilder sb = new StringBuilder();
        for (byte b : digest) sb.append(String.format("%02x", b));
        return sb.toString();
    }

    private static String csv(String s) {
        return "\"" + s.replace("\"", "\"\"") + "\"";
    }

    private static final class Arguments {
        final Path baseline;
        final Path variant;
        final Path opponent;
        final Path outputDir;
        final int pairs;
        final long baseSeed;
        final int timeoutSeconds;

        Arguments(Path baseline, Path variant, Path opponent, Path outputDir,
                  int pairs, long baseSeed, int timeoutSeconds) {
            this.baseline = baseline;
            this.variant = variant;
            this.opponent = opponent;
            this.outputDir = outputDir;
            this.pairs = pairs;
            this.baseSeed = baseSeed;
            this.timeoutSeconds = timeoutSeconds;
        }

        static Arguments parse(String[] args) {
            Path baseline = null, variant = null, opponent = null, output = null;
            int pairs = 3;
            long baseSeed = 2026101300L;
            int timeout = 20;

            for (int i = 0; i < args.length; i++) {
                switch (args[i]) {
                    case "--baseline" -> baseline = Path.of(args[++i]);
                    case "--variant" -> variant = Path.of(args[++i]);
                    case "--opponent" -> opponent = Path.of(args[++i]);
                    case "--output-dir" -> output = Path.of(args[++i]);
                    case "--pairs" -> pairs = Integer.parseInt(args[++i]);
                    case "--base-seed" -> baseSeed = Long.parseLong(args[++i]);
                    case "--timeout-seconds" -> timeout = Integer.parseInt(args[++i]);
                    default -> throw new IllegalArgumentException("Unknown argument: " + args[i]);
                }
            }

            if (baseline == null || variant == null || opponent == null || output == null) {
                throw new IllegalArgumentException(
                    "Required arguments: --baseline PATH --variant PATH --opponent PATH --output-dir PATH "
                    + "[--pairs N] [--base-seed N] [--timeout-seconds N]"
                );
            }
            if (pairs < 1 || pairs > 200) throw new IllegalArgumentException("--pairs must be 1..200");
            if (timeout < 5 || timeout > 120) throw new IllegalArgumentException("--timeout-seconds must be 5..120");
            return new Arguments(baseline, variant, opponent, output, pairs, baseSeed, timeout);
        }
    }
}
