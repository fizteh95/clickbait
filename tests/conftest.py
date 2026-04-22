import pytest
from pathlib import Path

from data.models import VideoMetric


CSV_CONTENT = """\
title,ctr,retention_rate,views,likes,avg_watch_time
Видео 1 clickbait,20.0,30,50000,1000,3.5
Видео 2 normal,10.0,70,30000,600,7.0
Видео 3 clickbait edge,15.5,39,40000,800,4.0
Видео 4 not clickbait ctr,14.0,25,20000,400,2.0
Видео 5 high retention,22.0,55,60000,1200,6.0
Видео 6 pure clickbait,25.0,20,80000,1600,2.5
Видео 7 borderline ctr,15.1,38,35000,700,3.8
Видео 8 retention exactly 40,18.0,40,45000,900,4.2
"""


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    path = tmp_path / "stats.csv"
    path.write_text(CSV_CONTENT, encoding="utf-8")
    return path


@pytest.fixture
def empty_csv(tmp_path: Path) -> Path:
    path = tmp_path / "empty.csv"
    path.write_text("title,ctr,retention_rate,views,likes,avg_watch_time\n", encoding="utf-8")
    return path


@pytest.fixture
def sample_videos() -> list[VideoMetric]:
    return [
        VideoMetric("Clickbait 1", 20.0, 30.0, 50000, 1000, 3.5),
        VideoMetric("Normal", 10.0, 70.0, 30000, 600, 7.0),
        VideoMetric("Pure clickbait", 25.0, 20.0, 80000, 1600, 2.5),
        VideoMetric("Borderline", 15.1, 38.0, 35000, 700, 3.8),
        VideoMetric("Just under 40", 18.0, 39.9, 45000, 900, 4.2),
    ]
