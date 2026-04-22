import pytest
from pathlib import Path

from main import main


class TestIntegration:
    def test_main_with_valid_files_and_report(self, sample_csv: Path, capsys) -> None:
        main(["--files", str(sample_csv), "--report", "clickbait"])
        captured = capsys.readouterr()
        assert "pure clickbait" in captured.out.lower()
        assert "clickbait" in captured.out.lower()

    def test_main_with_missing_file_exits_with_error(self, capsys) -> None:
        with pytest.raises(SystemExit) as exc_info:
            main(["--files", "/nonexistent.csv", "--report", "clickbait"])
        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "nonexistent.csv" in captured.err

    def test_main_with_invalid_report_exits_with_error(self, sample_csv: Path, capsys) -> None:
        with pytest.raises(SystemExit) as exc_info:
            main(["--files", str(sample_csv), "--report", "unknown"])
        assert exc_info.value.code == 1
        captured = capsys.readouterr()
        assert "Unknown report" in captured.err

    def test_main_with_empty_csv(self, empty_csv: Path, capsys) -> None:
        main(["--files", str(empty_csv), "--report", "clickbait"])
        captured = capsys.readouterr()
        assert "(no data)" in captured.out
