from abc import ABC, abstractmethod

from data.models import VideoMetric


class AbstractReport(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Unique identifier used as --report argument."""
        ...

    @abstractmethod
    def filter(self, videos: list[VideoMetric]) -> list[VideoMetric]:
        """Return videos that pass this report's criteria."""
        ...

    @abstractmethod
    def columns(self) -> list[str]:
        """Ordered list of column names to display."""
        ...
