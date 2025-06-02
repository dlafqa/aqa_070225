from get_browser import firefox
from first_po_classes import HomePage
from lesson_27_ex import exist_element, fill_input, clickable

def test_sign_in():
    driver = firefox(True)
    url = "https://guest:welcome2qauto@qauto.forstudy.space/"
    home_page = HomePage(driver, url)
    sign_btn = exist_element(driver, home_page.sign_in_btn[1])
    sign_btn.click()
    user = "user@gmail.com"
    password = "my supersecret password"
    fill_input(driver, home_page.login_fld[1], user)
    fill_input(driver, home_page.password_fld[1], password)
    assert clickable(driver, home_page.login_btn[1], 0.1)
    driver.close()