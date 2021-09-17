import unittest
from src.room import Room 
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Disco room", 30, 15)
        self.song1 = Song("closing time", "Semisonic")
        self.song2 = Song("All the small things", "Blink 182")

    def test_room_has_fee(self):
        self.assertEqual(15, self.room1.entry_fee)

    def test_can_add_song_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song2)
        self.assertEqual(2, len(self.room1.song_list) )