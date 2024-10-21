import time
import allure

from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.electronics_category_in_the_catalog import ElectronicsCategoryInTheCatalogPage
from pages.phones_and_gadgets_category_in_the_catalog import PhonesAndGadgetsCategoryInTheCatalogPage
from pages.smartphones_category_in_the_catalog_page import SmartphonesCategoryInTheCatalogPage


@allure.description("Test buy product")
def test_buy_product(login):
    driver = login

    print("Start Test")

    pa = PersonalAccountPage(driver)
    pa.go_to_the_main_page()

    mp = MainPage(driver)
    mp.go_to_the_catalog()

    ec_in_the_catalog = ElectronicsCategoryInTheCatalogPage(driver)
    ec_in_the_catalog.go_to_the_phones_and_gadgets()

    ph_in_the_catalog = PhonesAndGadgetsCategoryInTheCatalogPage(driver)
    ph_in_the_catalog.go_to_the_smartphones()

    smartphones_in_the_catalog = SmartphonesCategoryInTheCatalogPage(driver)
    smartphones_in_the_catalog.sorting_and_filtering_smartphones()
