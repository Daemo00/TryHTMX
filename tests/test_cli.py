"""Test CLI."""
import unittest

from TryHTMX.cli import main


class TestCLI(unittest.TestCase):
    """Test CLI."""

    def test_cli(self):
        """Test CLI."""
        args = str(5)
        self.assertEqual(main(args=args), 6)
