# class and logic for the first template
from main.models.guest import Guest
from main.models.template_base import InvitationTemplateBase
from main.models.wedding_info import WeddingInfo


class Template1(InvitationTemplateBase):
    guest_coord = (80, 100)
    def __init__(self,
                 guest: Guest,
                 wedding_info: WeddingInfo,
                 ):
        super().__init__(wedding_info,
                         "templates/assets/template1.jpg",
                         "templates/assets/fonts/arial.ttf",
                         font_size = 30,
                         groom_coord = (100, 100),
                         bride_coord = (150, 100),
                         date_coord = (400, 100),
                         location_coord = (400, 200)
                         )
        self.guest = guest


    def generate_invitation(self) -> str:
        data = self.fill_in_wedding_info()
        image = data["image"]
        draw = data["draw"]
        font = data["font"]

        draw.text(self.guest_coord, self.guest.full_name, font=font, fill='black')

        path = f"invites/template1_{self.guest.full_name}.jpg"
        image.save(path)
        return path
