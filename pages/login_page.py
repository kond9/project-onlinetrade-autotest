import allure

from configparser import ConfigParser
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class LoginPage(Base):
    url = 'https://www.onlinetrade.ru/member/login.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Config

    config_section = "data_auth"
    config = ConfigParser()
    config.read('config.ini')

    config_user_name = config.get(config_section, 'user_name')
    config_password = config.get(config_section, 'password')

    # Locators

    user_name = "//input[@name='login']"
    password = "//input[@name='password']"
    login_button = "//input[@name='submit']"
    main_word = "//span[@title='Мой профиль']"

    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Action

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("CLick login button")

    # Methods

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_user_name(self.config_user_name)
            self.input_password(self.config_password)
            self.click_login_button()
            self.assert_word(self.get_main_word(), "Мой профиль")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")
