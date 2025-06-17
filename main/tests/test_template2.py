import os

import pytest


from main.models.guest import Guest
from main.models.wedding_info import WeddingInfo
from main.templates.template2 import Template2
from main.utils.paths import get_base_dir

wed_info = WeddingInfo(bride_name="Kate Kate", groom_name="Tom Tom", date="23 september", location=" somewhere")

template_obj = Template2(Guest("Daniel Dan"), wed_info)

def test_fill_in():
    assert type(template_obj.fill_in_wedding_info()) == dict
    assert len(template_obj.fill_in_wedding_info().items()) == 3

def test_generate():
    assert template_obj.generate_invitation() == os.path.join(get_base_dir(), "main", "invites", "template2_Daniel_Dan.jpg")

if __name__ == "__main__":
    pytest.main()
