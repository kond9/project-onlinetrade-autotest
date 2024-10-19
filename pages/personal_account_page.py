from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class PersonalAccountPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    main_button = "//span[@itemprop='name']"
    main_word = "(//h2[@class='asH1'])[1]"

    # Getters

    def get_main_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Action

    def click_main_button(self):
        self.get_main_button().click()
        print("CLick main button")

    # Methods

    def go_to_the_main_page(self):
        with allure.step("Go to the main page"):
            Logger.add_start_step(method="go_to_the_main_page")
            self.get_current_url()
            self.click_main_button()
            self.assert_word(self.get_main_word(), "Акции")
            Logger.add_end_step(url=self.driver.current_url, method="go_to_the_main_page")
