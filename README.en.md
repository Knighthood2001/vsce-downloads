# vsce-downloads

[中文](README.md)

Fetch VSCode Marketplace extension download, install, and rating stats.

`vsce-downloads` can be used as a Python package or as a command line tool.

## Installation

Install from PyPI:

```bash
pip install vsce-downloads
```

Then import it in Python:

```python
import vsce_downloads
```

You can also use the `vsced` command line tool.

## Python Usage

Print formatted stats:

```python
from vsce_downloads import print_stats

print_stats("knighthood2001.ros2-quick-runner")
```

Example output:

```text
==== VSCode 插件统计信息 ====
插件名称：knighthood2001.ros2-quick-runner
总安装量：182
VSCode 编辑器内下载量：45
VSIX 离线包网页下载量：137
总更新次数：33
平均评分：暂无评分
评分人数：暂无评分
当日新增安装：0.0
周日均新增：0.00
月日均新增：0.00
```

Use `get_extension_stats()` if you want to process the data in your own code:

```python
from vsce_downloads import get_extension_stats

stats = get_extension_stats("knighthood2001.ros2-quick-runner")
print(stats["total_install"])
print(stats["vscode_download"])
print(stats["vsix_download"])
```

It returns a dictionary:

```python
{
    "vscode_download": 45,
    "vsix_download": 137,
    "total_install": 182,
    "update_count": 33,
    "trending_daily": 0.0,
    "trending_weekly": 0.0,
    "trending_monthly": 0.0,
    "average_rating": None,
    "rating_count": None,
}
```

## CLI Usage

Query a VSCode extension by its Marketplace id:

```bash
vsced knighthood2001.ros2-quick-runner
```

Print JSON for scripts:

```bash
vsced knighthood2001.ros2-quick-runner --json
```

Show the installed CLI version:

```bash
vsced --version
```

Example output:

```text
==== VSCode 插件统计信息 ====
插件名称：knighthood2001.ros2-quick-runner
总安装量：182
VSCode 编辑器内下载量：45
VSIX 离线包网页下载量：137
总更新次数：33
平均评分：暂无评分
评分人数：暂无评分
当日新增安装：0.0
周日均新增：0.00
月日均新增：0.00
```

## Development

Install from a local checkout:

```bash
pip install .
```

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
