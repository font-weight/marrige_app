# Guest class is here, it will contain all the information about a certain guest

class Guest:
    def __init__(self, full_name: str):
        self.full_name = full_name
        # in the future it's also possible to add email here to send invitations, that's why I created a different class