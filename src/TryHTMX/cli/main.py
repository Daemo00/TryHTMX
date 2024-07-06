"""CLI entry points."""
import argparse

from .app import add_parser as add_app_parser
from .db import add_parser as add_db_parser


def parse_args(args=None):
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        required=True,
    )

    add_app_parser(subparsers)
    add_db_parser(subparsers)
    return parser.parse_args(args=args)


def main(args=None):
    """Entry point for the CLI."""
    args = parse_args(args=args)
    return args.func(args)
