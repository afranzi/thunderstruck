import unittest

from thunderstruck.dummy import is_potato


class TestDummy(unittest.TestCase):
    def test_dummy(self):
        self.assertTrue(is_potato())
