import csv
import warnings
from pathlib import Path

from errors import CSVFileNotFoundError
from data.models import VideoMetric


def read_csv(path: str) -> list[VideoMetric]:
    p = Path(path)
    if not p.exists():
        raise CSVFileNotFoundError(path)

    videos: list[VideoMetric] = []
    with p.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                videos.append(VideoMetric.from_row(row))
            except (ValueError, KeyError) as exc:
                warnings.warn(f"Skipping malformed row: {row} ({exc})")
    return videos
