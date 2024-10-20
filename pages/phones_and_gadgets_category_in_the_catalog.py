from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class PhonesAndGadgetsCategoryInTheCatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    smartphones_button = "(//img[@alt='Смартфоны'])[1]"
    main_word = "//span[@class='breadcrumbs__itemCurrent']"

    # Getters

    def get_smartphones_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.smartphones_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Action

    def click_smartphones_button(self):
        self.get_smartphones_button().click()
        print("CLick smartphones button")

    # Methods

    def go_to_the_smartphones(self):
        with allure.step("Go to the smartphones"):
            Logger.add_start_step(method="go_to_the_smartphones")
            self.get_current_url()
            self.click_smartphones_button()
            self.assert_word(self.get_main_word(), "Смартфоны")
            Logger.add_end_step(url=self.driver.current_url, method="go_to_the_smartphones")
