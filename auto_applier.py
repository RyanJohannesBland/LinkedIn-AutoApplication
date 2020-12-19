import pdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def  main():
    # Instantiate a firefox instance.
    browser = webdriver.Firefox()
    # Get a query string of over 60k python software dev jobs.
    # TODO: Convert this to an interactive string generator.
    query_string = (
        "https://www.linkedin.com/jobs/search/?f_LF=f_AL&f_SB2=2&geoId=1036442"
        "78&keywords=python%20software%20developer&location=United%20States"
    )
    browser.get(query_string)
    main_page = authenticate(browser)
    models = filter_applications(main_page)


def filter_applications(browser):
    job_list_pane = browser.find_element_by_class_name("jobs-search-results")
    job_list = job_list.find_element_by_class_name(
        "jobs-search-results__list list-style-none")
    jobs = job_list.find_elements_by_tag_name("li")
    # TODO: Iterate through each job.
    # TODO: Apply algorithm to determine importance of given job listing.
    # TODO: Auto-apply/harvest valuable jobs.
    pdb.set_trace()
    pass


def authenticate(browser):
    # Press the sign up button.
    sign_up_button = browser.find_element_by_class_name(
        "nav__button-secondary")
    sign_up_button.send_keys(Keys.RETURN)
    # Wait for the new window to render. Grab username field once rendered.
    try:
        username_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
    except TimeoutError:
        browser.quit()

    # Add username and password.
    password_field = browser.find_element_by_id("password")
    # TODO: Abstract away my linkedin creds.
    username_field.send_keys()
    password_field.send_keys()

    # Press sign up button.
    sign_up_container = browser.find_element_by_class_name(
        "login__form_action_container")
    sign_up_button = sign_up_container.find_element_by_tag_name("button")
    sign_up_button.send_keys(Keys.RETURN)

    # TODO: Wait for new page to render.

    return browser


if __name__ == "__main__":
    main()