"""Tests para el módulo text_cmd."""

from __future__ import annotations

import pytest

from dev_utils_cli.commands.text_cmd import _convert

CONVERSIONS = [
    ("hello world", "snake", "hello_world"),
    ("hello world", "kebab", "hello-world"),
    ("hello world", "camel", "helloWorld"),
    ("hello world", "pascal", "HelloWorld"),
    ("hello-world_example", "snake", "hello_world_example"),
    ("hello_world", "kebab", "hello-world"),
    ("HelloWorld", "snake", "hello_world"),
    ("Mixed CASE Text", "title", "Mixed Case Text"),
    ("", "snake", ""),
]


@pytest.mark.parametrize("text,target,expected", CONVERSIONS)
def test_convert(text: str, target: str, expected: str) -> None:
    assert _convert(text, target) == expected
