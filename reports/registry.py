from errors import UnknownReportError
from reports.base import AbstractReport


class ReportRegistry:
    def __init__(self) -> None:
        self._reports: dict[str, AbstractReport] = {}

    def register(self, report: AbstractReport) -> None:
        self._reports[report.name] = report

    def get(self, name: str) -> AbstractReport:
        if name not in self._reports:
            raise UnknownReportError(name, list(self._reports.keys()))
        return self._reports[name]

    @property
    def available_reports(self) -> list[str]:
        return sorted(self._reports.keys())
