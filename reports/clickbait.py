from data.models import VideoMetric
from reports.base import AbstractReport


class ClickbaitReport(AbstractReport):
    name = "clickbait"

    def filter(self, videos: list[VideoMetric]) -> list[VideoMetric]:
        return [
            v for v in videos
            if v.ctr > 15 and v.retention_rate < 40
        ]

    def columns(self) -> list[str]:
        return ["title", "ctr", "retention_rate"]
