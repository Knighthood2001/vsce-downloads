import argparse
import json
import sys

import requests

from . import __version__
from .core import get_extension_stats, print_stats


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vsced",
        description="Fetch VSCode Marketplace extension download and rating stats.",
    )
    parser.add_argument(
        "extension_id",
        help="VSCode extension id, for example: ms-python.python",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print raw stats as JSON.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.json:
            stats = get_extension_stats(args.extension_id)
            print(json.dumps(stats, ensure_ascii=False, indent=2))
        else:
            print_stats(args.extension_id)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except requests.RequestException as exc:
        print(f"Request failed: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
