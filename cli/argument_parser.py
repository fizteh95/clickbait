import argparse
from typing import Optional


def parse_args(argv: Optional[list[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="YouTube video metrics report generator"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to one or more CSV files with video metrics",
    )
    parser.add_argument(
        "--report",
        type=str,
        required=True,
        help="Report name to generate (e.g. clickbait)",
    )
    return parser.parse_args(argv)
