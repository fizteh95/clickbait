from reports.clickbait import ClickbaitReport
from reports.registry import ReportRegistry

registry = ReportRegistry()
registry.register(ClickbaitReport())

__all__ = ["registry", "AbstractReport"]