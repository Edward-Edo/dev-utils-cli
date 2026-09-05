"""Tests para uuid_cmd."""

from __future__ import annotations

import re

from click.testing import CliRunner

from dev_utils_cli.cli import main


def test_single_uuid() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["uuid"])
    assert result.exit_code == 0
    uuid_value = result.output.strip()
    pattern = r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
    assert re.match(pattern, uuid_value)


def test_multiple_uuids() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["uuid", "-n", "5"])
    assert result.exit_code == 0
    assert len(result.output.strip().splitlines()) == 5


def test_no_dashes_upper() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["uuid", "-q", "-u"])
    assert result.exit_code == 0
    value = result.output.strip()
    assert "-" not in value
    assert value.isupper()
