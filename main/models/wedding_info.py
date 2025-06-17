# class for containing the information about wedding

class WeddingInfo:
    def __init__(self, bride_name: str = "",
                 groom_name: str = "",
                 date: str = "",
                 location: str = ""):
        self.bride_name = bride_name
        self.groom_name = groom_name
        self.date = date
        self.location = location