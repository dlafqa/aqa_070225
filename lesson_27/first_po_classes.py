from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.driver.get(url)
    
    sign_in_btn = (By.XPATH, '//button[@class="btn btn-outline-white header_signin"]')
    login_fld = (By.XPATH, '//*[@id="signinEmail"]')
    password_fld = (By.XPATH, '//*[@id="signinPassword"]')
    login_btn = (By.XPATH, '//button[@class="btn btn-primary"]')