import pdb

class Room:
    def __init__(self, input_name, input_capacity, input_entry_fee):
        self.name = input_name     
        self.capacity = input_capacity
        self.entry_fee = input_entry_fee
        self.song_list = []
        self.guest_list = []
        self.wait_queue_list = []

    def add_song_to_room(self, song):
        self.song_list.append(song)

    def check_find_guest_by_name(self, name):
        for guest in self.guest_list:
            if guest.name == name:
                return True
            return False

    def check_out(self, customer):
        is_in_list = self.check_find_guest_by_name(customer)
        if is_in_list == True:
            self.guest_list.remove(customer)
        if is_in_list == False:
            self.guest_list

    def can_guest_enter_this_room(self):
        if len(self.guest_list) < self.capacity:
            return True
        else: 
            return False

    def can_guest_afford_to_enter_room(self, customer):
        if customer.wallet >= self.entry_fee:
            return True
        else:
            return False

    def is_fav_song_in_this_room(self, customer):
        for song in self.song_list:
            if customer.fav_song == song.title:
                customer.talk = "woop"

    def guest_pays_entry_fee(self, customer):
        customer.wallet -= self.entry_fee

    def add_guest_to_guest_list(self, customer):
        self.guest_list.append(customer)


    def check_in(self, customer):
        if self.can_guest_enter_this_room() == True and self.can_guest_afford_to_enter_room(customer) == True:
            self.add_guest_to_guest_list(customer)
            self.guest_pays_entry_fee(customer)
            self.is_fav_song_in_this_room(customer)
        else:
            self.wait_queue_list.append(customer)

    def room_fee_total(self, room_list, amount):
        number_of_guests = len(room_list)
        return number_of_guests * amount



