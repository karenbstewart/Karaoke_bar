class Room:
    def __init__(self, input_name, input_capacity, input_entry_fee):
        self.name = input_name     
        self.capacity = input_capacity
        self.entry_fee = input_entry_fee
        self.song_list = []
        self.guest = []

    def add_song_to_room(self, song):
        self.song_list.append(song)

