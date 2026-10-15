#!/usr/bin/env python3
import sys
import verify_tetsuo_umezawa_approval_candidate_v2_once as verifier

# The repository serialization/order of the exact 14-swap candidate is authoritative.
verifier.SHA = '14ca66ceae4d634630a85aa1787731cfe840fd9fc2093bc37ad5dc17d1539ff6'

if __name__ == '__main__':
    sys.exit(verifier.main())
