import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# iніціалізуємо веб-драйвер
driver = Firefox()

# відкриття сторінки
driver.get("http://localhost/drop_down_menu.html")

dropbtn = driver.find_element(By.CLASS_NAME, "dropbtn")
submenu = driver.find_element(By.CLASS_NAME, "submenu")
product_links = driver.find_elements(By.CLASS_NAME, "product-link")

actions = ActionChains(driver)

for link in product_links:
    # Навести на "Menu"
    actions.move_to_element(dropbtn).perform()
    
    # Навести на "Products"
    actions.move_to_element(submenu).perform()
    
    # Тепер посилання видиме — клік
    actions.move_to_element(link).click().perform()
    
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        print("Alert did not appear")