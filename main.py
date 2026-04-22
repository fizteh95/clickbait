import sys
from typing import Optional

from cli.argument_parser import parse_args
from data.reader import read_csv
from errors import CSVFileNotFoundError, UnknownReportError
from output.table import render_table
from reports import registry


def main(argv: Optional[list[str]] = None) -> None:
    args = parse_args(argv)

    all_videos = []
    for path in args.files:
        try:
            all_videos.extend(read_csv(path))
        except CSVFileNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    try:
        report = registry.get(args.report)
    except UnknownReportError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    filtered = report.filter(all_videos)
    filtered_sorted = sorted(filtered, key=lambda v: v.ctr, reverse=True)

    rows = [
        {col: getattr(v, col) for col in report.columns()}
        for v in filtered_sorted
    ]
    render_table(rows, report.columns())


if __name__ == "__main__":
    main()
