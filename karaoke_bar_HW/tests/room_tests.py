import unittest
from src.room import Room 
from src.song import Song
from src.guest import Guest
import pdb

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Disco room", 13, 15)
        self.room2 = Room("RnB room", 10, 20)
        self.room3 = Room("ickle room", 4, 25)
        self.song1 = Song("closing time", "Semisonic")
        self.song2 = Song("All the small things", "Blink 182")
        self.song3 = Song("Call it dreaming", "Iron & Wine")
        self.guest1 = Guest("Dan", 100, "closing time")
        self.guest2 = Guest("Björn", 150, "Hooked on a feeling")
        self.guest3 = Guest("Jimi", 12, "Purple Haze")
        self.guest4 = Guest("Thomas", 300, "Die a happy man")
        self.guest5 = Guest("Mark", 3, "If")
        self.guest6 = Guest("Samuel", 1000, "Call it dreaming")
        self.guest7 = Guest("Ray", 80, "Days")

    def test_room_has_fee(self):
        self.assertEqual(15, self.room1.entry_fee)

    def test_can_add_song_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song2)
        self.assertEqual(2, len(self.room1.song_list))

    def test_check_in(self):
        self.room1.check_in(self.guest1)
        self.assertEqual(1 , len(self.room1.guest_list))

    def test_guest_has_checked_in(self):
        self.room1.check_in(self.guest1)
        is_guest_checked_in = self.room1.check_find_guest_by_name(self.guest1.name) 
        self.assertEqual(True , is_guest_checked_in)

    def test_guest_has_checked_out(self):
        self.room2.check_in(self.guest1)
        self.room2.check_in(self.guest2)
        self.room2.check_out(self.guest2)
        is_guest_checked_out = self.room2.check_find_guest_by_name(self.guest2.name)
        self.assertEqual(False, is_guest_checked_out)

    def test_too_many_guest_in_room(self):
        self.room3.check_in(self.guest1)
        self.room3.check_in(self.guest2)
        self.room3.check_in(self.guest3)
        self.room3.check_in(self.guest4)
        self.room3.check_in(self.guest5)
        self.room3.check_in(self.guest6)
        self.room3.check_in(self.guest7)
        self.assertEqual(3, len(self.room3.wait_queue_list))
        self.assertEqual(4, len(self.room3.guest_list))

    def test_guest_in_room_paid(self):
        self.room2.check_in(self.guest1)
        self.room2.check_in(self.guest3)
        self.assertEqual(80, self.guest1.wallet)
        self.assertEqual(12, self.guest3.wallet)

    def test_plays_guests_favourite_song(self):
        self.room3.add_song_to_room(self.song3)
        self.room3.add_song_to_room(self.song1)
        self.room3.add_song_to_room(self.song2)
        self.room3.check_in(self.guest1)
        self.room3.is_fav_song_in_this_room(self.guest1)
        self.assertEqual("woop", self.guest1.talk)
        
    def test_total_of_fees_paid_for_room(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest2)
        self.room1.check_in(self.guest3)
        self.room1.check_in(self.guest4)
        self.room1.check_in(self.guest5)
        self.assertEqual(45, self.room1.room_fee_total(self.room1.guest_list, self.room1.entry_fee))



