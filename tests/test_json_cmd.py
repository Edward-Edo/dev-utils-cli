"""Tests para json_cmd."""

from __future__ import annotations

import json

from click.testing import CliRunner

from dev_utils_cli.cli import main


def test_format_valid_json() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["json", "-i", '{"b":1,"a":2}', "--no-color"])
    assert result.exit_code == 0
    parsed = json.loads(result.output)
    assert parsed == {"b": 1, "a": 2}


def test_minify_json() -> None:
    runner = CliRunner()
    raw = '{\n  "a": 1,\n  "b": 2\n}'
    result = runner.invoke(main, ["json", "-i", raw, "--minify", "--no-color"])
    assert result.exit_code == 0
    assert result.output.strip() == '{"a":1,"b":2}'


def test_sort_keys() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["json", "-i", '{"b":2,"a":1}', "--sort-keys", "--no-color"])
    assert result.exit_code == 0
    assert result.output.startswith('{\n  "a": 1')


def test_invalid_json() -> None:
    runner = CliRunner()
    result = runner.invoke(main, ["json", "-i", "{invalid}", "--no-color"])
    assert result.exit_code == 1
