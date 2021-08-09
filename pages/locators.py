from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password1"]')
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '[value="Add to basket"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] h1')
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, '[class="alertinner "] strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
    BASKET_TOTAL = (By.CSS_SELECTOR, '[class="alertinner "] p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[id="messages"] [class="alert alert-safe alert-noicon alert-success  fade in"]:nth-child(1)')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    UPPER_BASKET_BUTTON = (By.CSS_SELECTOR, '[class="btn-group"] [class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '[class="basket-items"]')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
