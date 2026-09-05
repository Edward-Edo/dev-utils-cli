"""Tests para hash_cmd."""

from __future__ import annotations

from click.testing import CliRunner

from dev_utils_cli.cli import main


def test_sha256_basic() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["hash", "-i", "hello", "-a", "sha256"])
    assert result.exit_code == 0
    assert (
        result.output.strip()
        == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    )


def test_all_algorithms() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["hash", "-i", "abc", "--all"])
    assert result.exit_code == 0
    assert "MD5" in result.output
    assert "SHA256" in result.output
    assert "900150983cd24fb0d6963f7d28e17f72" in result.output  # md5("abc")
