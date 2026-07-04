# vsce-downloads

[中文](README.md)

Fetch VSCode Marketplace extension download, install, and rating stats.

`vsce-downloads` can be used as a Python package or as a command line tool.
After installation it provides the `vsced` command.

## Installation

Install from a local checkout:

```bash
pip install .
```

Install from a built wheel:

```bash
pip install dist/vsce_downloads-0.1.0-py3-none-any.whl
```

## CLI Usage

Query a VSCode extension by its Marketplace id:

```bash
vsced ms-python.python
```

Print JSON for scripts:

```bash
vsced ms-python.python --json
```

Show the installed CLI version:

```bash
vsced --version
```

Example output:

```text
==== VSCode 插件统计信息 ====
总安装量：123456
VSCode 编辑器内下载量：120000
VSIX 离线包网页下载量：3456
总更新次数：789
平均评分：4.5
评分人数：100
当日新增安装：12.0
周日均新增：34.00
月日均新增：56.00
```

## Python Usage

```python
from vsce_downloads import get_extension_stats, print_stats

print_stats("ms-python.python")

stats = get_extension_stats("ms-python.python")
print(stats["total_install"])
```

`get_extension_stats()` returns a dictionary:

```python
{
    "vscode_download": 120000,
    "vsix_download": 3456,
    "total_install": 123456,
    "update_count": 789,
    "trending_daily": 12.0,
    "trending_weekly": 34.0,
    "trending_monthly": 56.0,
    "average_rating": 4.5,
    "rating_count": 100,
}
```

## Development

Build source and wheel distributions:

```bash
python3 -m build
```

If your local Python environment does not have `venv` or a new enough
`setuptools`, this legacy command can also build the package:

```bash
python3 setup.py sdist bdist_wheel
```

Generated files are written to `dist/`.

## Project Metadata

- Package name: `vsce-downloads`
- Import name: `vsce_downloads`
- CLI command: `vsced`
- Python: `>=3.7`
- Runtime dependency: `requests>=2.25.0`
