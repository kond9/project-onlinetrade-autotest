import allure

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class PersonalAccountPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    main_button = "//span[@itemprop='name']"
    basket_button = "//div[@class='huab__cell huab__cell__multicart js__header__basketCover ']"
    main_word = "(//h2[@class='asH1'])[1]"
    basket_word = "//h1"

    # Getters

    def get_main_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_button)))

    def get_basket_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.basket_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_basket_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.basket_word)))

    # Action

    def click_main_button(self):
        self.get_main_button().click()
        print("CLick main button")

    def click_basket_button(self):
        self.get_basket_button().click()
        print("CLick basket button")

    # Methods

    def go_to_the_main_page(self):
        with allure.step("Go to the main page"):
            Logger.add_start_step(method="go_to_the_main_page")
            self.get_current_url()
            self.click_main_button()
            self.assert_word(self.get_main_word(), "Акции")
            Logger.add_end_step(url=self.driver.current_url, method="go_to_the_main_page")

    def go_to_the_basket_page(self):
        with allure.step("Go to the basket page"):
            Logger.add_start_step(method="go_to_the_basket_page")
            self.get_current_url()
            self.click_basket_button()
            self.assert_word(self.get_basket_word(), "Корзина")
            Logger.add_end_step(url=self.driver.current_url, method="go_to_the_basket_page")
