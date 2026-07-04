# vsce-downloads

[中文](README.md)

Fetch download counts, installation statistics, ratings and other metrics for extensions hosted on the VS Code Marketplace.

`vsce-downloads` can be used both as a Python library and a command-line tool.

## Installation

Install from PyPI:

```bash
pip install vsce-downloads
```

After installation, you can import it in your Python project:

```python
import vsce_downloads
```

You can also use the CLI tool `vsced` directly in your terminal.

## How to Get Your VS Code Extension ID

1. From the VS Code Marketplace extension detail page



2. From your locally installed extensions panel in VS Code



## Python Usage

Pass your VS Code extension ID to print formatted statistics:

```python
from vsce_downloads import print_stats

print_stats("knighthood2001.urdf-formatting")
```

Sample output:

```text
==== VSCode 扩展统计信息 ====
扩展ID：knighthood2001.urdf-formatting
总安装量：1270
VSCode 编辑器内下载量：919
VSIX 离线包网页下载量：351
总更新次数：146
平均评分：5.0
评分人数：1
当日新增安装：0.0
周日均新增：1.09
月日均新增：4.58
```

If you need to process the raw data programmatically, use `get_extension_stats()`:

```python
from vsce_downloads import get_extension_stats

stats = get_extension_stats("knighthood2001.urdf-formatting")
print(stats["total_install"])
print(stats["vscode_download"])
print(stats["vsix_download"])
```

Returned dictionary structure:

```python
{
  "vscode_download": 919,
  "vsix_download": 351,
  "total_install": 1270,
  "update_count": 146,
  "trending_daily": 0.0,
  "trending_weekly": 1.0893246187363834,
  "trending_monthly": 4.57516339869281,
  "average_rating": 5.0,
  "rating_count": 1
}
```

## Command Line Usage

Query statistics with your VS Code extension ID:

```bash
vsced knighthood2001.urdf-formatting
```

Output raw JSON for script integration:

```bash
vsced knighthood2001.urdf-formatting --json
```

Sample JSON output:

```json
{
  "vscode_download": 919,
  "vsix_download": 351,
  "total_install": 1270,
  "update_count": 146,
  "trending_daily": 0.0,
  "trending_weekly": 1.0893246187363834,
  "trending_monthly": 4.57516339869281,
  "average_rating": 5.0,
  "rating_count": 1
}
```

Check the installed CLI version:

```bash
vsced --version
```

## Development & Packaging

Install from source for local development:

```bash
pip install .
```

Build source distribution and wheel package:

```bash
python3 -m build
```

If your environment lacks `venv` or uses an older `setuptools` version, use the legacy build command:

```bash
python3 setup.py sdist bdist_wheel
```

Built artifacts will be generated under the `dist/` directory.

## Project Information

- PyPI Package Name: `vsce-downloads`
- Python Import Name: `vsce_downloads`
- CLI Command: `vsced`
- Python Version Requirement: `>=3.7`
- Dependency: `requests>=2.25.0`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.