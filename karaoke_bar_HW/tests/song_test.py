import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("closing time", "Semisonic")
        self.song2 = Song("All the small things", "Blink 182")

    def test_song_title(self):
        self.assertEqual("closing time", self.song1.title)
    