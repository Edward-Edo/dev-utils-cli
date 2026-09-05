"""Comandos de la CLI dev-utils-cli."""

from __future__ import annotations

import click
from rich.console import Console
from rich.table import Table

from .commands import base64_cmd, hash_cmd, json_cmd, text_cmd, uuid_cmd

console = Console()


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(package_name="dev-utils-cli", prog_name="devu")
def main() -> None:
    """🛠️  dev-utils-cli — utilidades rápidas para desarrolladores."""


@main.command(name="info")
def info() -> None:
    """Muestra información del entorno y comandos disponibles."""
    table = Table(title="dev-utils-cli · comandos", show_header=True, header_style="bold magenta")
    table.add_column("Comando", style="cyan", no_wrap=True)
    table.add_column("Descripción", style="white")

    rows = [
        ("json", "Formatea, valida y minimiza JSON."),
        ("hash", "Genera hashes (md5, sha1, sha256, sha512)."),
        ("base64", "Codifica/decodifica en Base64."),
        ("uuid", "Genera uno o varios UUID v4."),
        ("text", "Convierte entre casos (snake, kebab, camel, pascal)."),
        ("info", "Muestra esta ayuda."),
    ]
    for cmd, desc in rows:
        table.add_row(cmd, desc)
    console.print(table)


main.add_command(json_cmd.json_cmd)
main.add_command(hash_cmd.hash_cmd)
main.add_command(base64_cmd.base64_cmd)
main.add_command(uuid_cmd.uuid_cmd)
main.add_command(text_cmd.text_cmd)


if __name__ == "__main__":
    main()
