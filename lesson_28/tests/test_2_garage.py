

def test_add_car(home_page, garage_page):
    guest_login = home_page.item(home_page.guest_login)
    assert guest_login.is_clickable()
    guest_login.click()
    add_car = home_page.item(garage_page.add_car)
    assert add_car.is_visible()
    add_car.click()
    brand_select = home_page.item(garage_page.brand)
    add_btn = home_page.item(garage_page.add)
    brand_select.select("Ford")
    mileage_input = home_page.item(garage_page.mileage)
    mileage_input.send_keys("1")
    add_btn.click()
    