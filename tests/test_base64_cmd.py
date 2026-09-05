"""Tests para base64_cmd."""

from __future__ import annotations

import base64

from click.testing import CliRunner

from dev_utils_cli.cli import main


def test_encode_decode_roundtrip() -> None:
    runner = CliRunner()
    text = "Hola mundo 🌍"

    encoded = runner.invoke(main, ["base64", "-e", "-i", text])
    assert encoded.exit_code == 0
    expected = base64.b64encode(text.encode()).decode()
    assert encoded.output.strip() == expected

    decoded = runner.invoke(main, ["base64", "-d", "-i", expected])
    assert decoded.exit_code == 0
    assert decoded.output.strip() == text


def test_decode_invalid() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["base64", "-d", "-i", "!!!not-base64!!!"])
    assert result.exit_code == 1
