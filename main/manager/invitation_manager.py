# Here is the basic logic of the application
from main.models.guest import Guest
from main.models.wedding_info import WeddingInfo


class InvitationManager:
    def __init__(self):
        self.guests = []
        self.wedding_info = WeddingInfo() # create for now empty WeddingInfo object

        # _________________________THIS MUST BE IMPLEMENTED________________
        # self.template = Template1() # default template will be number 1

    def add_guest(self, full_name: str):
        # add guests to the list
        self.guests.append(Guest(full_name))


    # ______________HAS TO BE TESTED_____________________
    def remove_guest(self, full_name: str):
        for guest in self.guests:
            if full_name == guest.full_name:
                self.guests.remove(guest)
                return 1

        return 0

    def view_guests(self):
        # returns a list if all the names of the guests
        return [guest.full_name for guest in self.guests]






