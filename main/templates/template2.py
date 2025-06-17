# class and logic for the first template
import os

from main.models.guest import Guest
from main.models.template_base import InvitationTemplateBase
from main.models.wedding_info import WeddingInfo
from main.utils.paths import get_base_dir


# here in this template for example I dont want to have guest's name, that's why I used polymorphism
class Template2(InvitationTemplateBase):
    image_path = os.path.join(get_base_dir(), "main", "templates", "assets", "template2.jpg")
    font_path = os.path.join(get_base_dir(), "main", "templates", "assets", "fonts", "arial.ttf")

    def __init__(self,
                 guest: Guest,
                 wedding_info: WeddingInfo,
                 ):

        super().__init__(wedding_info,
                         self.image_path,
                         self.font_path,
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

        path = os.path.join(get_base_dir(), "main", "invites",
                            f"template2_{self.guest.full_name.replace(" ", "_")}.jpg")

        # create dir if there is no one
        dir_path = os.path.dirname(path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        image.save(path)
        return path
