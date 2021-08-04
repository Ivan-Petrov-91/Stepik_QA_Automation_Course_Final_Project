from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '[value="Add to basket"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] h1')
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, '[class="alertinner "] strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
    BASKET_TOTAL = (By.CSS_SELECTOR, '[class="alertinner "] p strong')
