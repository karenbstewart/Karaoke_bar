import unittest
from src.guest import Guest 

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("John", 100)

    def guest_has_name(self):
        self.assertEqual("John", self.guest.name)