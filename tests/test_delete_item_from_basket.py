import allure

from pages.personal_account_page import PersonalAccountPage
from pages.basket_page import BasketPage


@allure.description("Test delete item from basket")
def test_delete_item_from_basket(driver, login):

    print("Start Test")

    pa = PersonalAccountPage(driver)
    pa.go_to_the_basket_page()

    bp = BasketPage(driver)
    bp.delete_item()
