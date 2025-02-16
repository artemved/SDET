import pytest
import time
import os
from selenium import webdriver
from pages.form_page import FormPage

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(1)
    driver.save_screenshot("form.png")
    time.sleep(3)
    driver.quit()

def test_form_submission(browser):
    browser.get("https://demoqa.com/automation-practice-form")
    form_page = FormPage(browser)

    form_page.fill_first_name("Artem")
    form_page.fill_last_name("Vedmenskiy")
    form_page.fill_email("artem.v@gmail.com")
    form_page.select_gender("Male")
    form_page.fill_mobile("0123456789")
    form_page.select_date_of_birth("22", "May", "1989")
    form_page.fill_subjects(["Chemistry", "Computer Science"])
    form_page.select_hobbies(["Sports", "Reading", "Music"])
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "cat.jpg"))
    form_page.upload_picture(file_path)
    form_page.fill_current_address("126 Street, Samara")
    form_page.select_state("NCR")
    form_page.select_city("Delhi")
    form_page.submit_form()

    confirmation_message = form_page.get_confirmation_message()
    assert "Thanks for submitting the form" in confirmation_message
