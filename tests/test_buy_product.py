import time
import allure

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.electronics_category_in_the_catalog import ElectronicsCategoryInTheCatalogPage
from pages.phones_and_gadgets_category_in_the_catalog import PhonesAndGadgetsCategoryInTheCatalogPage


@allure.description("Test buy product")
def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    print("Start Test")

    login = LoginPage(driver)
    login.authorization()

    pa = PersonalAccountPage(driver)
    pa.go_to_the_main_page()

    mp = MainPage(driver)
    mp.go_to_the_catalog()

    ec_in_the_catalog = ElectronicsCategoryInTheCatalogPage(driver)
    ec_in_the_catalog.go_to_the_phones_and_gadgets()

    ph_in_the_catalog = PhonesAndGadgetsCategoryInTheCatalogPage(driver)
    ph_in_the_catalog.go_to_the_smartphones()

    driver.quit()
