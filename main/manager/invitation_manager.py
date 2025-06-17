# Here is the basic logic of the application
from main.models.guest import Guest
from main.models.wedding_info import WeddingInfo
from main.templates.template1 import Template1
from main.templates.template2 import Template2


class InvitationManager:
    def __init__(self):
        self.guests = []
        self.wedding_info = None # make it for now empty
        self.template = Template1 # default template will be number 1

    def add_guest(self, full_name: str) -> bool:
        # add guests to the list
        if len(full_name) > 30:
            return False

        if not all(c.isalpha() or c.isspace() or c.isdigit() for c in full_name):
            return False

        self.guests.append(Guest(full_name))
        return True



    def remove_guest(self, full_name: str) -> bool:
        for guest in self.guests:
            if full_name == guest.full_name:
                self.guests.remove(guest)
                return True

        return False



    def view_guests(self) -> list:
        # returns a list if all the names of the guests
        return [guest.full_name for guest in self.guests]


    def set_wedding_info(self, bride_name: str = "",
                         groom_name: str = "",
                         date: str = "",
                         location: str = "") -> bool:
        if (len(bride_name) > 25) or (len(groom_name) > 25) or (len(date) > 20) or (len(location) > 50):
            return False

        self.wedding_info = WeddingInfo(bride_name, groom_name, date, location)
        return True




    def choose_template(self, number: int) -> bool:
        if number == 1:
            self.template = Template1
            return True
        elif number == 2:
            self.template = Template2
            return True

        else:
            return False


    def generate_all_invitations(self):
        if not self.guests or not self.wedding_info:
            return False

        count = 0
        for guest in self.guests:
            self.template(guest, self.wedding_info).generate_invitation()
            count += 1

        return count






