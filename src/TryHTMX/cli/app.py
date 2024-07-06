"""Command Line Interface for App."""
from ..app.run import run


def execute(args=None):
    """Run app with `args`."""
    return run(
        mode=args.mode,
    )


def add_parser(subparsers):
    """Parse App arguments."""
    parser = subparsers.add_parser("app")
    parser.set_defaults(func=execute)
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
