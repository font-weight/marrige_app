# the base for templates, it's for polymorphism :))
from guest import  Guest
from wedding_info import WeddingInfo
from abc import ABC, abstractmethod


class InvitationTemplateBase(ABC):
    def __init__(self,
                 guest: Guest,
                 wedding_info: WeddingInfo
                 ):
        self.guest = guest
        self.wedding_info = wedding_info


    @abstractmethod
    def generate_invitation(self):
        pass