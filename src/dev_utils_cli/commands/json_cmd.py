"""Comando: json — formatea, valida y minimiza JSON."""

from __future__ import annotations

import json
import sys
from typing import TextIO

import click
from rich.console import Console
from rich.syntax import Syntax

console = Console(stderr=True)


def _read_input(input_arg: str | None) -> str:
    if input_arg is not None:
        return input_arg
    if sys.stdin.isatty():
        click.echo(click.get_current_context().get_help(), err=True)
        click.echo("\n[ERROR] Proporciona --input o pasa JSON por stdin.", err=True)
        sys.exit(2)
    return sys.stdin.read()


@click.command(name="json")
@click.option("-i", "--input", "input_text", default=None, help="JSON como string.")
@click.option(
    "-o",
    "--output",
    type=click.Path("w", encoding="utf-8", dir_okay=False),
    default=None,
    help="Escribe el resultado en un archivo.",
)
@click.option("--indent", type=int, default=2, show_default=True, help="Espacios de indentación.")
@click.option("--minify", is_flag=True, help="Salida en una sola línea.")
@click.option("--sort-keys", is_flag=True, help="Ordena las claves del objeto.")
@click.option("--no-color", is_flag=True, help="Desactiva el resaltado de sintaxis.")
def json_cmd(  # noqa: A001 — nombre del comando CLI
    input_text: str | None,
    output: TextIO | None,
    indent: int,
    minify: bool,
    sort_keys: bool,
    no_color: bool,
) -> None:
    """Formatea, valida y minimiza JSON desde --input o stdin."""
    raw = _read_input(input_text)
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        console.print(f"[bold red]✗ JSON inválido:[/] {exc.msg} (línea {exc.lineno}, col {exc.colno})")
        sys.exit(1)

    if minify:
        result = json.dumps(data, separators=(",", ":"), sort_keys=sort_keys, ensure_ascii=False)
        click.echo(result)
        return

    pretty = json.dumps(data, indent=indent, sort_keys=sort_keys, ensure_ascii=False)

    if output:
        output.write(pretty + "\n")
        output.close()
        console.print(f"[green]✓[/] Escrito en {output.name}")
        return

    if no_color or not sys.stdout.isatty():
        click.echo(pretty)
        return

    syntax = Syntax(pretty, "json", theme="monokai", line_numbers=False, word_wrap=True)
    console.print(syntax)
