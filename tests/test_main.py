"""Test Main."""
import unittest

from TryHTMX.main import add_one


class TestMain(unittest.TestCase):
    """Test Main."""

    def test_add_one(self):
        """Test Main."""
        self.assertEqual(add_one(5), 6)
