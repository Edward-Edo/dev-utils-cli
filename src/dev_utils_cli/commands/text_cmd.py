"""Comando: text — conversor entre casos (snake, kebab, camel, pascal, upper, lower)."""

from __future__ import annotations

import re
import sys

import click

CASES = ("snake", "kebab", "camel", "pascal", "upper", "lower", "title")


def _normalize(text: str) -> list[str]:
    parts = re.split(r"[\s_\-]+", text)
    return [p for p in parts if p]


def _convert(text: str, target: str) -> str:
    tokens = _normalize(text)
    if not tokens:
        return ""

    if target == "snake":
        return "_".join(t.lower() for t in tokens)
    if target == "kebab":
        return "-".join(t.lower() for t in tokens)
    if target == "camel":
        return tokens[0].lower() + "".join(t.capitalize() for t in tokens[1:])
    if target == "pascal":
        return "".join(t.capitalize() for t in tokens)
    if target == "upper":
        return text.upper()
    if target == "lower":
        return text.lower()
    if target == "title":
        return " ".join(t.capitalize() for t in tokens)
    return text


@click.command(name="text")
@click.option("-i", "--input", "input_text", default=None, help="Texto de entrada.")
@click.option(
    "-t",
    "--to",
    "target",
    type=click.Choice(CASES, case_sensitive=False),
    required=True,
    help="Caso destino.",
)
def text_cmd(input_text: str | None, target: str) -> None:
    """Convierte texto entre snake, kebab, camel, pascal, upper, lower, title."""
    if input_text is None:
        if sys.stdin.isatty():
            click.echo(click.get_current_context().get_help(), err=True)
            sys.exit(2)
        input_text = sys.stdin.read()
    click.echo(_convert(input_text, target.lower()))
