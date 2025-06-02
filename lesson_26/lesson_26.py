from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Ініціалізація веб-драйвера
driver = webdriver.Firefox()

# Відкриття веб-сторінки
driver.get("http://localhost")

# Робота з веб-елементами і виконання дій на сторінці
user_field = driver.find_element(By.ID, "username")
pass_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login_button")
user_field.send_keys("Hello world!")
li_elements = driver.find_elements(By.TAG_NAME, "li")
for li in li_elements:
    print("Знайдено елемент:", li.text)


driver.get("http://localhost/demo.html")
user_field = driver.find_element(By.XPATH, "//input[@id='username']")
pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
log_button = driver.find_element(By.XPATH, "//button[@id='submit']")
pass_field.send_keys("Supper password!")
male_radio = driver.find_element(By.ID, "male")
male_radio.click()
newsletter_checkbox = driver.find_element(By.ID, "newsletter")
newsletter_checkbox.click()

# Вибір значення з випадаючого списку за ID
country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_visible_text("США")
# country_dropdown.select_by_value("usa")

driver.get("http://localhost/frame.html")
button = driver.find_element(By.XPATH, '//*[@id="myid"]')
print(button.is_displayed())
driver.switch_to.frame(driver.find_element(By.ID, "myFrame"))
youtube = driver.find_element(By.XPATH,'//*[@title="YouTube video player"]')
print(youtube.is_displayed())
# Закриття браузера
driver.switch_to.default_content()
button.click()
driver.quit()