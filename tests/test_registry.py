import pytest

from errors import UnknownReportError
from reports import registry


class TestReportRegistry:
    def test_register_and_get(self) -> None:
        from reports.clickbait import ClickbaitReport
        r = registry.get("clickbait")
        assert isinstance(r, ClickbaitReport)

    def test_get_unknown_raises_UnknownReportError(self) -> None:
        with pytest.raises(UnknownReportError) as exc_info:
            registry.get("nonexistent")
        assert exc_info.value.name == "nonexistent"
        assert "clickbait" in exc_info.value.available

    def test_available_reports_contains_clickbait(self) -> None:
        assert "clickbait" in registry.available_reports
