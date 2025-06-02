

def test_homepage_menu(home_page):
    homepage_menu = home_page.item(home_page.menu_home)
    assert homepage_menu.is_visible(), f"Not found element: {homepage_menu._locator}"

def test_homepage_sign_in(home_page):
    element = home_page.item(home_page.sign_in_button)
    assert element.is_visible(), f"Not found: {element._locator}"


def test_login_as_guest(home_page, garage_page):
    guest_login = home_page.item(home_page.guest_login)
    assert guest_login.is_clickable()
    guest_login.click()
    add_car = home_page.item(garage_page.add_car)
    assert add_car.is_visible()
    add_car.highlight_and_make_screenshot("addcar.png")
