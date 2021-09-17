import unittest
from src.guest import Guest 

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("John", 100, "closing time")

    def test_guest_has_name(self):
        self.assertEqual("John", self.guest1.name)