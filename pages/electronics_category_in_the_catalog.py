import allure

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class ElectronicsCategoryInTheCatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    phones_and_gadgets_button = "//img[@alt='Телефоны и гаджеты']"
    main_word = "//span[@class='breadcrumbs__itemCurrent']"

    # Getters

    def get_phones_and_gadgets_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phones_and_gadgets_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Action

    def click_phones_and_gadgets_button(self):
        self.get_phones_and_gadgets_button().click()
        print("CLick phones and gadgets button")

    # Methods

    def go_to_the_phones_and_gadgets(self):
        with allure.step("Go to the phones and gadgets"):
            Logger.add_start_step(method="go_to_the_phones_and_gadgets")
            self.get_current_url()
            self.click_phones_and_gadgets_button()
            self.assert_word(self.get_main_word(), "Телефоны и гаджеты")
            Logger.add_end_step(url=self.driver.current_url, method="go_to_the_phones_and_gadgets")
