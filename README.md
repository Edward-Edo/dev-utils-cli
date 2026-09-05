# 🛠️ dev-utils-cli

[![CI](https://github.com/Edward-Edo/dev-utils-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/Edward-Edo/dev-utils-cli/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Ruff](https://img.shields.io/badge/code%20style-ruff-261230)](https://github.com/astral-sh/ruff)

Una **CLI rápida, elegante y sin dependencias pesadas** con utilidades diarias para desarrolladores: formateo de JSON, hashes, Base64, UUIDs y conversión entre casos de texto. Construida con [Click](https://click.palletsprojects.com/) + [Rich](https://rich.readthedocs.io/).

---

## ✨ Características

- 🧾 **json** — formatea, valida, minimiza y reordena JSON desde CLI o stdin.
- 🔐 **hash** — md5, sha1, sha256 y sha512.
- 🔁 **base64** — codifica/decodifica con validación estricta.
- 🆔 **uuid** — uno o varios UUID v4, con o sin guiones.
- 🔤 **text** — convierte entre `snake`, `kebab`, `camel`, `pascal`, `upper`, `lower`, `title`.
- 🎨 **Output enriquecido** en terminales compatibles (Rich), plano en pipes.
- ✅ Testeada con `pytest`, lint con `ruff`, CI multi-versión en GitHub Actions.

---

## 📦 Instalación

### Desde el código fuente

```bash
git clone https://github.com/Edward-Edo/dev-utils-cli.git
cd dev-utils-cli
pip install -e ".[dev]"
```

Esto instala el comando `devu` globalmente en tu entorno.

### Requisitos

- Python **3.9+**
- `pip` actualizado

---

## 🚀 Uso rápido

```bash
# Ayuda general
devu --help

# JSON: formatear entrada de stdin
echo '{"b":1,"a":2}' | devu json --sort-keys

# Hash SHA-256
devu hash -i "hola mundo"

# Todos los hashes de un texto
devu hash -i "abc" --all

# Base64 encode / decode
devu base64 -e -i "Hola mundo"
echo "SG9sYSBtdW5kbw==" | devu base64 -d

# Generar 5 UUIDs sin guiones y en mayúsculas
devu uuid -n 5 -q -u

# Convertir casos
devu text -i "HelloWorld example-case" -t snake
# -> hello_world_example_case

devu text -i "hello_world_example" -t camel
# -> helloWorldExample
```

---

## 🧪 Tests y lint

```bash
pip install -e ".[dev]"
ruff check src tests
pytest
pytest --cov=dev_utils_cli --cov-report=term-missing
```

---

## 🗂️ Estructura del proyecto

```
dev-utils-cli/
├── src/dev_utils_cli/
│   ├── __init__.py
│   ├── cli.py
│   └── commands/
│       ├── __init__.py
│       ├── base64_cmd.py
│       ├── hash_cmd.py
│       ├── json_cmd.py
│       ├── text_cmd.py
│       └── uuid_cmd.py
├── tests/
│   ├── test_base64_cmd.py
│   ├── test_hash_cmd.py
│   ├── test_json_cmd.py
│   ├── test_text_cmd.py
│   └── test_uuid_cmd.py
├── .github/workflows/ci.yml
├── pyproject.toml
├── LICENSE
├── .gitignore
└── README.md
```

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Haz fork y crea una rama: `git checkout -b feature/mi-mejora`
2. Asegúrate de pasar lint y tests: `ruff check . && pytest`
3. Abre un Pull Request describiendo el cambio.

---

## 📄 Licencia

[MIT](LICENSE) © 2026 Edward Itriago

---

## ✍️ Autor

**Edward Itriago** — Full Stack Developer
📧 edwarditriagosub@gmail.com
🔗 [github.com/Edward-Edo](https://github.com/Edward-Edo)
