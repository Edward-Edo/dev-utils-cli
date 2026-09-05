"""Comando: hash — genera hashes de un texto."""

from __future__ import annotations

import hashlib
import sys

import click
from rich.console import Console
from rich.table import Table

console = Console(stderr=True)

ALGORITHMS = ("md5", "sha1", "sha256", "sha512")


@click.command(name="hash")
@click.option("-i", "--input", "input_text", default=None, help="Texto a hashear.")
@click.option(
    "-a",
    "--algorithm",
    type=click.Choice(ALGORITHMS, case_sensitive=False),
    default="sha256",
    show_default=True,
    help="Algoritmo de hash.",
)
@click.option("--all", "all_algos", is_flag=True, help="Genera todos los algoritmos soportados.")
def hash_cmd(input_text: str | None, algorithm: str, all_algos: bool) -> None:
    """Genera el hash de un texto (md5, sha1, sha256, sha512)."""
    if input_text is None:
        if sys.stdin.isatty():
            click.echo(click.get_current_context().get_help(), err=True)
            sys.exit(2)
        input_text = sys.stdin.read()

    data = input_text.encode("utf-8")
    algorithms = ALGORITHMS if all_algos else (algorithm.lower(),)

    if all_algos:
        table = Table(title="Hashes", show_header=True, header_style="bold magenta")
        table.add_column("Algoritmo", style="cyan", no_wrap=True)
        table.add_column("Hash", style="white")
        for algo in algorithms:
            digest = hashlib.new(algo, data).hexdigest()
            table.add_row(algo.upper(), digest)
        console.print(table)
        return

    digest = hashlib.new(algorithm.lower(), data).hexdigest()
    click.echo(digest)
