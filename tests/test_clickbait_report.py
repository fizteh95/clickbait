import pytest

from data.models import VideoMetric
from reports.clickbait import ClickbaitReport


class TestClickbaitReport:
    @pytest.fixture
    def report(self) -> ClickbaitReport:
        return ClickbaitReport()

    def test_filter_returns_only_matching_videos(
        self, report: ClickbaitReport, sample_videos: list[VideoMetric]
    ) -> None:
        result = report.filter(sample_videos)
        assert len(result) == 4
        titles = {v.title for v in result}
        assert "Clickbait 1" in titles
        assert "Pure clickbait" in titles
        assert "Borderline" in titles
        assert "Just under 40" in titles

    def test_filter_returns_empty_when_none_match(self, report: ClickbaitReport) -> None:
        videos = [
            VideoMetric("Low CTR", 10.0, 30.0, 1000, 10, 1.0),
            VideoMetric("High Retention", 20.0, 50.0, 1000, 10, 1.0),
        ]
        assert report.filter(videos) == []

    def test_columns_returns_correct_fields(
        self, report: ClickbaitReport
    ) -> None:
        assert report.columns() == ["title", "ctr", "retention_rate"]
