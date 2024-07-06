"""Command Line Interface for DB."""
from ..orm.main import populate


def execute(args=None):
    """Run DB with `args`."""
    if args.populate:
        populate()


def add_parser(subparsers):
    """Parse DB arguments."""
    parser = subparsers.add_parser("db")
    parser.set_defaults(func=execute)
    parser.add_argument(
        "--populate",
        type=bool,
        default=True,
    )
    return parser
