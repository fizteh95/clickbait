class CSVFileNotFoundError(FileNotFoundError):
    def __init__(self, path: str) -> None:
        self.path = path
        super().__init__(f"File not found: {path}")


class UnknownReportError(ValueError):
    def __init__(self, name: str, available: list[str]) -> None:
        self.name = name
        self.available = available
        super().__init__(
            f"Unknown report '{name}'. Available reports: {', '.join(available)}"
        )
