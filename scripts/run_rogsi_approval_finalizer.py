from pathlib import Path

source_path = Path(__file__).with_name("finalize_rogsi_approval_once.py")
source = source_path.read_text(encoding="utf-8")
old = "\n audit = audit_path.read_text(encoding=\"utf-8\")"
new = "\naudit = audit_path.read_text(encoding=\"utf-8\")"
if old not in source:
    raise SystemExit("Expected RogSi finalizer syntax defect not found")
source = source.replace(old, new, 1)
namespace = {
    "__name__": "__main__",
    "__file__": str(source_path),
    "__package__": None,
}
exec(compile(source, str(source_path), "exec"), namespace)
