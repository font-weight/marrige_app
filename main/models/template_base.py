# the base for templates, it's for polymorphism :))

from wedding_info import WeddingInfo
from abc import ABC, abstractmethod
from PIL import Image, ImageDraw, ImageFont


class InvitationTemplateBase(ABC):
    # this base class will fill in only information about the wedding,
    # but not about guest, because we might want to invite the whole family in some templates
    def __init__(self,
                 wedding_info: WeddingInfo,
                 image_path: str,
                 font_path: str,
                 font_size: int,
                 groom_coord,
                 bride_coord,
                 date_coord,
                 location_coord
                 ):
        self.wedding_info = wedding_info
        self.image_path = image_path
        self.font_path = font_path
        self.font_size = font_size
        self.groom_coord = groom_coord
        self.bride_coord = bride_coord
        self.date_coord = date_coord
        self.location_coord = location_coord

    def fill_in_wedding_info(self):
        image = Image.open(self.image_path).convert("RGB")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(self.font_path, self.font_size)
        draw.text(self.groom_coord, self.wedding_info.groom_name, font=font, fill='black')
        draw.text(self.bride_coord, self.wedding_info.bride_name, font=font, fill='black')
        draw.text(self.date_coord, self.wedding_info.date, font=font, fill='black')
        draw.text(self.location_coord, self.wedding_info.location, font=font, fill='black')

        return {"image": image, "draw": draw, "font": font}


    @abstractmethod
    def generate_invitation(self):
        pass