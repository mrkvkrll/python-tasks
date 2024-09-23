import re


def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.home_phone == clear(contact_from_edit_page.home_phone)
    assert contact_from_homepage.phone == clear(contact_from_edit_page.phone)
    assert contact_from_homepage.work_phone == clear(contact_from_edit_page.work_phone)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.phone == contact_from_edit_page.phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone


def clear(s):
    return re.sub("[-() ]", "", s)


