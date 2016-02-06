
from model.contact import Contact

def test_add_empty_contact(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    app.contact_helper.add(Contact())
    app.session_helper.logout()

def test_add_contact(app):
    app.wd_helper.open_home_page(app)
    app.session_helper.login(login="admin", pwd="secret")
    #fill all fields with '123' value
    app.contact_helper.add(Contact('123'))
    app.session_helper.logout()



