"""CLI entry points."""
import argparse


from .main import run


def parse_args(args=None):
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        "-m",
        choices=[
            "dev",
            "prod",
        ],
        default="dev",
    )
    return parser.parse_args(args=args)


def main(args=None):
    """Entry point for the application script."""
    args = parse_args(args=args)
    return run(
        mode=args.mode,
    )
