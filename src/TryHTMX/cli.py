"""CLI entry points."""
import argparse


from .main import run


def run_app(args=None):
    """Run app with `args`."""
    return run(
        mode=args.mode,
    )


def add_app_parser(subparsers):
    """Parse App arguments."""
    parser = subparsers.add_parser("app")
    parser.set_defaults(func=run_app)
    parser.add_argument(
        "--mode",
        "-m",
        choices=[
            "dev",
            "prod",
        ],
        default="dev",
    )
    return parser


def run_db(args=None):
    """Run DB with `args`."""
    return run(
        mode=args.mode,
    )


def add_db_parser(subparsers):
    """Parse DB arguments."""
    parser = subparsers.add_parser("db")
    parser.set_defaults(func=run_db)
    parser.add_argument(
        "populate",
        type=bool,
        default=True,
    )
    return parser


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
