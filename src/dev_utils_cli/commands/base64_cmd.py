"""Comando: base64 — codifica y decodifica texto en Base64."""

from __future__ import annotations

import base64
import binascii
import sys

import click


def _read_stdin_or_arg(value: str | None) -> str:
    if value is not None:
        return value
    if sys.stdin.isatty():
        click.echo(click.get_current_context().get_help(), err=True)
        sys.exit(2)
    return sys.stdin.read()


@click.command(name="base64")
@click.option("-e", "--encode", "mode", flag_value="encode", default=True, help="Codifica (default).")
@click.option("-d", "--decode", "mode", flag_value="decode", help="Decodifica.")
@click.option("-i", "--input", "input_text", default=None, help="Texto de entrada.")
def base64(mode: str, input_text: str | None) -> None:
    """Codifica o decodifica texto en Base64."""
    raw = _read_stdin_or_arg(input_text)
    data = raw.encode("utf-8")

    try:
        if mode == "encode":
            click.echo(base64.b64encode(data).decode("ascii"))
        else:
            click.echo(base64.b64decode(data, validate=True).decode("utf-8"))
    except (binascii.Error, UnicodeDecodeError) as exc:
        click.echo(f"[ERROR] Entrada Base64 inválida: {exc}", err=True)
        sys.exit(1)
