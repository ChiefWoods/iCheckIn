from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from dotenv import load_dotenv
import os
import time
import argparse
import re

load_dotenv()

parser = argparse.ArgumentParser(description='iCheckIn Automation')
parser.add_argument('checkin_code', type=str, help='iCheckIn code')


class Browser:
    browser, service = None, None

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    # navigate to page url
    def goto(self, url: str):
        self.browser.get(url)

    # close the browser
    def close(self):
        self.browser.quit()

    # find element by attribute and modify its content
    def add_input(self, by: By, value: str, text: str):
        input = self.browser.find_element(by=by, value=value)
        input.send_keys(text)
        time.sleep(1)

    # find element by attribute and click it
    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    # login to iZone
    def login(self, username: str, password: str):
        self.add_input(by=By.ID, value='student_uid', text=username)
        self.add_input(by=By.ID, value='password', text=password)
        self.click_button(by=By.ID, value='submit')

    # go to iCheckIn page and check in
    def enter_code(self, code: str):
        while not re.match(r'^\d{5}$', code):
            code = input('Invalid code. Please enter a 5 digit code: ')

        self.add_input(by=By.ID, value='checkin_code', text=code)
        self.click_button(by=By.ID, value='iCheckin')

    # check into class
    def check_in(self, code: str):
        notification, check_in_success = None, False

        while not check_in_success:
            self.enter_code(code)
            notification = self.browser.find_element(
                by=By.ID, value='notification')
            check_in_success = 'alert-success' in notification.get_attribute(
                'class')

            if not check_in_success:
                print('Error:', notification.text)
                code = input("Enter new code: ")

        print('Success:', notification.text)


if __name__ == '__main__':
    args = parser.parse_args()

    browser = Browser('drivers/chromedriver.exe')
    browser.goto('https://izone.sunway.edu.my/login')
    browser.login(os.getenv('STUDENT_ID'), os.getenv('PASSWORD'))
    browser.goto('https://izone.sunway.edu.my/icheckin')
    browser.check_in(args.checkin_code)

    input("Press 'Enter' to close the browser...")
    browser.close()
