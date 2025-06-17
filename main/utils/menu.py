from random import choices

from main.manager.invitation_manager import InvitationManager


class Interface:
    title = "\033[1;33mWhat do you want to do?\033[0m"

    def __init__(self, manager: InvitationManager):
        self.manager = manager


    choices = ["1. Change information about the marriage",
               "2. Add a guest",
               "3. Remove guest by name",
               "4. View the guests list",
               "5. Choose template",
               "6. Generate invitations!",
               "0. Exit",
               ""]


    def show_the_choices(self):
        for line in self.choices:
            print(f"\033[1;32m{line}\033[0m")

    def get_answer(self):
        self.answer = 0
        while True:
            self.answer = input("\033[1;37mI want: \033[0m")

            if self.answer.isdigit():
                self.answer = int(self.answer)

                if self.answer == 1:
                    self.set_wedding_info()
                elif self.answer == 2:
                    self.add_guest()
                elif self.answer == 3:
                    self.remove_guest()
                elif self.answer == 4:
                    self.view_guests()
                elif self.answer == 5:
                    self.choose_template()
                elif self.answer == 6:
                    self.generate_invitations()
                elif self.answer == 0:
                    print("\033[1;34mAll the best!\033[0m \n")
                    return 0
                else:
                    continue
                break



            print("\033[1;31mEnter a number!\033[0m")




    def set_wedding_info(self):

        while True:
            result = self.manager.set_wedding_info(
                input("\033[1;33mCongrads! Please enter Bride's name (no more than 25 symbols): \033[0m"),
                input("\033[1;33mEnter Groom's name (no more than 25 symbols): \033[0m"),
                input("\033[1;33mEnter date (no more than 20 symbols): \033[0m"),
                input("\033[1;33mEnter location (no more than 50 symbols): \033[0m")
            )

            if not result:
                print("\033[1;31mPlease respect the restrictions!\033[0m\n\n")
            else:
                print("\033[1;32mInformation was successfully added\033[0m\n\n")
                break


    def add_guest(self):
        while True:
            result = self.manager.add_guest(input("\033[1;33mWrite guest's full name (no more than 30 symbols and special symbols are not allowed): \033[0m"))

            if not result:
                print("\033[1;31mPlease respect the restrictions!\033[0m\n\n")
            else:
                print("\033[1;32mInformation was successfully added\033[0m\n\n")
                break

    def remove_guest(self):
        if self.manager.remove_guest(input("\033[1;33mWrite guest's full name to delete: \033[0m")):
            print("\033[1;32mThe guest was successfully deletes\033[0m\n\n")
        else:
            print("\033[1;31mThere is no such guest!\033[0m\n\n")


    def view_guests(self):
        print(f"\033[1;36mGuests:\033[0m")

        for name in self.manager.view_guests():
            print(f"\033[1;36m  {name}\033[0m")

        print("\n")



if __name__ == "__main__":
    manager = InvitationManager()

    interface = Interface(manager)
    while True:
        print(interface.title)
        interface.show_the_choices()
        if(interface.get_answer() == 0):
            break







