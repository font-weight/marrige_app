import pytest

from main.manager.invitation_manager import InvitationManager
from main.templates.template1 import Template1
from main.templates.template2 import Template2


def test_add_guest():
    manager = InvitationManager()
    assert manager.add_guest("Somebody Some")
    assert len(manager.guests) == 1
    assert manager.guests[0].full_name == "Somebody Some"

    assert manager.add_guest("Somebody Some 2")
    assert manager.add_guest("Somebody Some 2")
    assert len(manager.guests) == 3
    assert manager.guests[1].full_name == "Somebody Some 2"
    assert manager.add_guest("Toooooo long name more than thirty letters") == False
    assert manager.add_guest("Name with other symbols .") == False
    assert manager.add_guest(".") == False
    assert manager.add_guest("1e2") == True
    assert manager.add_guest("Fjsaaf@") == False


def test_remove_guest():
    manager = InvitationManager()
    assert manager.remove_guest("Somebody Some") == False
    manager.add_guest("Somebody Some")
    assert manager.remove_guest("Somebody Some")
    manager.add_guest("Somebody Some")
    manager.add_guest("Somebody Some")
    assert manager.remove_guest("Somebody Some")
    assert len(manager.guests) == 1
    assert manager.remove_guest("Somebody Some")
    assert len(manager.guests) == 0



def test_view_guests():
    manager = InvitationManager()

    assert manager.view_guests() == []

    manager.add_guest("Somebody Some")
    assert manager.view_guests() == ["Somebody Some"]
    manager.remove_guest("Somebody Some")
    assert manager.view_guests() == []

    manager.add_guest("Somebody Some")
    manager.add_guest("Somebody Some")
    assert manager.view_guests() == ["Somebody Some","Somebody Some"]


def test_set_wedding_info():
    manager = InvitationManager()

    assert not manager.wedding_info
    assert manager.set_wedding_info("Bride Bride", "Groom Groom", "date date", "location")
    assert manager.wedding_info

    assert manager.wedding_info.bride_name == "Bride Bride"
    assert manager.wedding_info.groom_name == "Groom Groom"
    assert manager.wedding_info.date == "date date"
    assert manager.wedding_info.location == "location"

    assert manager.set_wedding_info("Br", "Gr", "dt", "lc")
    assert manager.wedding_info.bride_name == "Br"

    assert manager.set_wedding_info("Toooooo long namjklle asdfasdjkljljk") == False
    assert manager.wedding_info.bride_name == "Br"
    assert manager.set_wedding_info(groom_name="Tooooo long name again dsafsd") == False


def test_choose_template():
    manager = InvitationManager()

    assert manager.template == Template1
    assert manager.choose_template(1)
    assert manager.template == Template1
    assert manager.choose_template(2)
    assert manager.template == Template2
    assert manager.choose_template(3) == False
    assert manager.choose_template(3414234) == False
    assert manager.choose_template(0) == False
    assert manager.choose_template(-12412) == False

def test_generate_all_invitations():
    manager = InvitationManager()

    assert manager.generate_all_invitations() == False
    manager.add_guest("Somebody")
    assert manager.generate_all_invitations() == False
    manager.remove_guest("Somebody")
    manager.set_wedding_info()
    assert manager.generate_all_invitations() == False
    manager.add_guest("Somebody")
    assert manager.generate_all_invitations() == 1
    manager.add_guest("Somebody1")
    manager.add_guest("Somebody2")
    manager.add_guest("Somebody3")
    assert manager.generate_all_invitations() == 4

    manager.set_wedding_info("Bride Bride", "Groom Groom", "date date", "location")
    assert manager.generate_all_invitations() == 4

    manager.choose_template(2)
    assert manager.generate_all_invitations() == 4





