from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class FormPage:
    def __init__(self, browser):
        self.browser = browser

    def fill_first_name(self, first_name):
        self.browser.find_element(By.ID, "firstName").send_keys(first_name)

    def fill_last_name(self, last_name):
        self.browser.find_element(By.ID, "lastName").send_keys(last_name)

    def fill_email(self, email):
        self.browser.find_element(By.ID, "userEmail").send_keys(email)

    def select_gender(self, gender):
        self.browser.find_element(By.XPATH, f"//label[text()='{gender}']").click()

    def fill_mobile(self, mobile):
        self.browser.find_element(By.ID, "userNumber").send_keys(mobile)

    def select_date_of_birth(self, day, month, year):
        date_of_birth_input = self.browser.find_element(By.ID, "dateOfBirthInput")
        date_of_birth_input.click()
        time.sleep(1)

        year_dropdown = self.browser.find_element(By.CLASS_NAME, "react-datepicker__year-select")
        year_dropdown.send_keys(year)
        time.sleep(1)

        month_dropdown = self.browser.find_element(By.CLASS_NAME, "react-datepicker__month-select")
        month_dropdown.send_keys(month)
        time.sleep(1)

        day_element = self.browser.find_element(By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
        day_element.click()
        time.sleep(1)

    def fill_subjects(self, subjects):
        subjects_input = self.browser.find_element(By.ID, "subjectsInput")
        for subject in subjects:
            subjects_input.send_keys(subject)
            time.sleep(1)
            subjects_input.send_keys(Keys.ARROW_DOWN)
            subjects_input.send_keys(Keys.ENTER)
            time.sleep(1)

    def select_hobbies(self, hobbies):
        for hobby in hobbies:
            self.browser.find_element(By.XPATH, f"//label[text()='{hobby}']").click()

    def upload_picture(self, file_path):
        self.browser.find_element(By.ID, "uploadPicture").send_keys(file_path)

    def fill_current_address(self, address):
        self.browser.find_element(By.ID, "currentAddress").send_keys(address)

    def select_state(self, state):
        self.browser.find_element(By.ID, "react-select-3-input").send_keys(state + "\n")

    def select_city(self, city):
        self.browser.find_element(By.ID, "react-select-4-input").send_keys(city + "\n")

    def submit_form(self):
        self.browser.find_element(By.ID, "submit").click()

    def get_confirmation_message(self):
        return self.browser.find_element(By.ID, "example-modal-sizes-title-lg").text
