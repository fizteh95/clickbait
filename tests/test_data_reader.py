import pytest
from pathlib import Path

from data.reader import read_csv
from errors import CSVFileNotFoundError


class TestDataReader:
    def test_read_csv_parses_all_rows(self, sample_csv: Path) -> None:
        videos = read_csv(str(sample_csv))
        assert len(videos) == 8
        assert videos[0].title == "Видео 1 clickbait"
        assert videos[0].ctr == 20.0
        assert videos[0].retention_rate == 30.0

    def test_read_csv_raises_on_missing_file(self) -> None:
        with pytest.raises(CSVFileNotFoundError):
            read_csv("/nonexistent/path/stats.csv")

    def test_read_csv_skips_malformed_rows(self, tmp_path: Path) -> None:
        content = """\
title,ctr,retention_rate,views,likes,avg_watch_time
Good video,18.0,35,50000,1000,4.0
Bad row,abc,35,50000,1000,4.0
Another good,20.0,25,60000,1200,3.5
"""
        path = tmp_path / "malformed.csv"
        path.write_text(content, encoding="utf-8")
        videos = read_csv(str(path))
        assert len(videos) == 2
        assert videos[0].title == "Good video"
        assert videos[1].title == "Another good"
