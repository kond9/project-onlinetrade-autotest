import allure

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_button = "//a[@class='header__button header__buttonCatalog  js__catalogLine__mainLink ']"
    electronic_category_button = "//a[@data-catid='5293']"
    main_word = "//span[@class='breadcrumbs__itemCurrent']"

    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_electronic_category_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.electronic_category_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Action

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("CLick catalog button")

    def click_electronic_category_button(self):
        self.get_electronic_category_button().click()
        print("CLick electronic category button")

    # Methods

    def go_to_the_catalog(self):
        with allure.step("Go to the catalog"):
            Logger.add_start_step(method="go_to_the_catalog")
            self.get_current_url()
            self.click_catalog_button()
            self.click_electronic_category_button()
            self.assert_word(self.get_main_word(), "Электроника")
            Logger.add_end_step(url=self.driver.current_url, method="go_to_the_catalog")
