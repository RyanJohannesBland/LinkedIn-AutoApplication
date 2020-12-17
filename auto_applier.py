import pdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser = webdriver.Firefox()
browser.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&f_SB2=2&geoId=103644278&keywords=python%20software%20developer&location=United%20States")

sign_up_button = browser.find_element_by_class_name("nav__button-secondary")
sign_up_button.send_keys(Keys.RETURN)
try:
    username_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
except TimeoutError:
    browser.quit()

password_field = browser.find_element_by_id("password")
username_field.send_keys()
password_field.send_keys()

sign_up_container = browser.find_element_by_class_name("login__form_action_container")
sign_up_button = sign_up_container.find_element_by_tag_name("button")
sign_up_button.send_keys(Keys.RETURN)