

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

    def check_in(self, customer):
        if len(self.guest_list) <= self.capacity:
            self.guest_list.append(customer)
        if len(self.guest_list) > self.capacity:
            self.wait_queue_list.append(customer)

    def check_find_guest_by_name(self, name):
        for guest in self.guest_list:
            if guest.name == name:
                return True
            return False

    def check_out(self, singer):
        is_in_list = self.check_find_guest_by_name(singer)
        if is_in_list == True:
            self.guest_list.remove(singer)
        if is_in_list == False:
            self.guest_list

    # def can_guest_enter_this_room(self, customer, wait_list):


    


