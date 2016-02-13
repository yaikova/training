import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        print('create new fixture')
        fixture = Application()
        fixture.wd_helper.open_home_page()
        fixture.session_helper.login_as_admin()
    else:
        if not fixture.is_valid():
            print('rebuild broken fixture')
            fixture = Application()
            fixture.wd_helper.open_home_page()
            fixture.session_helper.login_as_admin()
    return fixture


@pytest.fixture(scope = 'session', autouse = True)
def finish(request):
    def fin():
        fixture.session_helper.logout()
        fixture.destroy()
        print('Finish test session')
    request.addfinalizer(fin)



