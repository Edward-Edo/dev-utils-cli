"""Comando: uuid — genera UUIDs v4."""

from __future__ import annotations

import uuid

import click


@click.command(name="uuid")
@click.option(
    "-n",
    "--count",
    type=click.IntRange(min=1),
    default=1,
    show_default=True,
    help="Cantidad de UUIDs a generar.",
)
@click.option(
    "-u",
    "--upper",
    is_flag=True,
    help="Devuelve el UUID en mayúsculas.",
)
@click.option(
    "-q",
    "--no-dashes",
    is_flag=True,
    help="Elimina los guiones del UUID.",
)
def uuid_cmd(count: int, upper: bool, no_dashes: bool) -> None:
    """Genera uno o varios UUID v4."""
    for _ in range(count):
        value = str(uuid.uuid4())
        if no_dashes:
            value = value.replace("-", "")
        if upper:
            value = value.upper()
        click.echo(value)
