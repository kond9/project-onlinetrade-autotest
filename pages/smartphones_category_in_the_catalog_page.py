from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class SmartphonesCategoryInTheCatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    sort_button = "//select[@id='js__listingSort_ID']"
    price_items = "//span[@itemprop='price']"
    filter_availability_button = "//label[@for='f1d2185d7198ca866f057607628f90f1e']"
    show_all_producers_button = "//*[@id='columnBlock__producersFilterIDfilter__ID']/div[2]/div/a"
    input_producer = "//input[@data-filterid='producersFilterID']"
    filter_producer_button = "//label[@for='f2a409a83fa51c7453545eb0e379d7926']"
    filter_OS_button = "//label[@for='f67a28eca5ca68297064467458f38d803']"
    filter_internal_memory_button = "//label[@for='f77edb32393ed9592a633d06859632e56']"
    filter_hertz_button = "//label[@for='fc4f68bdb53b079153cea31bdaefe40e1']"
    show_filtered_smartphones_button = "//a[@title='Показать товары по выбранным условиям']"
    buy_button = "//*[@id='item_container_3187758__ID']/div[3]/div[3]/a"
    arrange_order_button = "//a[@id='js__popup_addedToCart__cartLinkID']"
    main_word = "//a[@data-popupcaption='Подтверждение очистки корзины']"

    # Getters

    def get_sort_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.sort_button)))

    def get_price_items(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.price_items)))

    def get_filter_availability_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_availability_button)))

    def get_show_all_producers_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.show_all_producers_button)))

    def get_input_producer(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.input_producer)))

    def get_filter_producer_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_producer_button)))

    def get_filter_OS_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_OS_button)))

    def get_filter_internal_memory_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_internal_memory_button)))

    def get_filter_hertz_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_hertz_button)))

    def get_show_filtered_smartphones_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.show_filtered_smartphones_button)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_arrange_order_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.arrange_order_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Action

    def click_sort_button(self):
        self.get_sort_button().click()
        self.get_sort_button().send_keys(Keys.ARROW_DOWN)
        self.get_sort_button().send_keys(Keys.RETURN)
        print("CLick sort button")

    def check_prices(self):
        list_elements_price = self.get_price_items()
        list_price = []
        translation_table = str.maketrans('', '', " ₽")
        for price in list_elements_price:
            list_price.append(price.text.translate(translation_table))
        sorted_list_price = sorted(list_price, key=int, reverse=True)
        if list_price == sorted_list_price:
            print("Check prices")

    def click_filter_availability_button(self):
        self.get_filter_availability_button().click()
        print("CLick filter availability button")

    def click_show_all_producers_button(self):
        self.get_show_all_producers_button().click()
        print("Show all producers button")

    def click_input_producer(self):
        self.get_input_producer().click()
        self.get_input_producer().send_keys("APPLE")
        print("Click input button")

    def click_filter_producer_button(self):
        self.get_filter_producer_button().click()
        print("CLick filter producer button")

    def click_filter_OS_button(self):
        self.get_filter_OS_button().click()
        print("CLick filter OS button")

    def click_filter_internal_memory_button(self):
        self.get_filter_internal_memory_button().click()
        print("CLick filter internal memory button")

    def click_filter_hertz_button(self):
        self.get_filter_hertz_button().click()
        print("CLick filter hertz button")

    def click_show_filtered_smartphones_button(self):
        self.get_show_filtered_smartphones_button().click()
        print("CLick show filtered smartphones button")

    def click_buy_button(self):
        self.get_buy_button().click()
        print("CLick buy button")

    def click_arrange_order_button(self):
        self.get_arrange_order_button().click()
        print("CLick arrange order button")

    # Methods

    def sorting_and_filtering_smartphones(self):
        with allure.step("Sorting and filtering smartphones"):
            Logger.add_start_step(method="sorting_and_filtering_smartphones")
            self.get_current_url()
            self.click_sort_button()
            self.check_prices()
            self.click_filter_availability_button()
            self.click_show_all_producers_button()
            self.click_input_producer()
            self.click_filter_producer_button()
            self.click_filter_OS_button()
            self.click_filter_internal_memory_button()
            self.click_filter_hertz_button()
            self.click_show_filtered_smartphones_button()
            self.click_buy_button()
            self.click_arrange_order_button()
            self.assert_word(self.get_main_word(), "Очистить корзину")
            Logger.add_end_step(url=self.driver.current_url, method="sorting_and_filtering_smartphones")
