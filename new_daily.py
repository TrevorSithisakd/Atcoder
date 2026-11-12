"""Create a folder for today's AtCoder Daily Training session.

Usage:
    python new_daily.py 16:00            -> Daily_Training_EASY_2026_11_12_1600
    python new_daily.py 18:00 medium     -> Daily_Training_MEDIUM_2026_11_12_1800

Windows folder names can't contain '/' or ':', so
"AtCoder Daily Training EASY 2026/11/12 16:00start" becomes
"Daily_Training_EASY_2026_11_12_1600".
"""
import argparse
import re
from datetime import date
from pathlib import Path

LEVELS = ["easy", "medium", "hard", "all"]

parser = argparse.ArgumentParser(description="Create a Daily Training folder.")
parser.add_argument("time", help="start time, e.g. 16:00, 1600 or 16")
parser.add_argument("level", nargs="?", default="easy", choices=LEVELS,
                    type=str.lower, help="difficulty (default: easy)")
args = parser.parse_args()

m = re.fullmatch(r"(\d{1,2}):?(\d{2})?", args.time)
if not m or int(m[1]) > 23 or int(m[2] or 0) > 59:
    parser.error(f"invalid time {args.time!r}; use HH:MM, e.g. 16:00")
hhmm = f"{int(m[1]):02d}{m[2] or '00'}"

name = f"Daily_Training_{args.level.upper()}_{date.today():%Y_%m_%d}_{hhmm}"
folder = Path(__file__).resolve().parent / name

if folder.exists():
    print(f"Already exists: {folder}")
else:
    folder.mkdir()
    print(f"Created: {folder}")
