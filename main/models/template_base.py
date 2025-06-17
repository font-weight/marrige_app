# the base for templates, it's for polymorphism :))
from guest import  Guest
from wedding_info import WeddingInfo

class InvitationTemplateBase:
    # each template will have each own realization of generating method
    def generate_invitation(self, guest: Guest, wedding_info: WeddingInfo):
        pass