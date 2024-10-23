import allure

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class BasketPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    delete_button = "//a[@class='ic__set ic__set__closeThick js__ajaxExchange']"
    confirm_delete_button = "//a[@class='button button__orange js__linkDeleteBasketItem']"
    main_word = "//*[@id='main_area']/div[4]/div/div[3]/p[3]"

    # Getters

    def get_delete_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.delete_button)))

    def get_confirm_delete_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.confirm_delete_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.main_word)))

    # Action

    def click_delete_button(self):
        self.get_delete_button().click()
        print("Click delete button")

    def click_confirm_delete_button(self):
        self.get_confirm_delete_button().click()
        print("CLick confirm delete button")

    # Methods

    def delete_item(self):
        with allure.step("Delete item"):
            Logger.add_start_step(method="delete_item")
            self.get_current_url()
            self.click_delete_button()
            self.click_confirm_delete_button()
            self.assert_word(self.get_main_word(),
                             "Стикер в шапке сайта всегда покажет вам, с какой корзиной вы работаете в данный момент — теперь у каждой корзины свой цвет и своё название. Состояние других корзин легко увидеть просто наведя мышку на стикер.")
            Logger.add_end_step(url=self.driver.current_url, method="delete_item")
