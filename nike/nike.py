import os
import time
import nike.constants as const
import random

import undetected_chromedriver as uc
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

class Nike(uc.Chrome):
    def __init__(self, config) -> None:
        '''Instantiate the bot and webdriver object'''
        options = uc.ChromeOptions()
        options.add_argument('proxy-server=xxx.xxx.x.xx:xxxx')
        options.add_argument('--user-data-dir=C:path')
        super(Nike, self).__init__(use_subprocess=True, options=options)
        self.username = config.get("NIKE_ACCOUNT", "USERNAME")
        self.password = config.get("NIKE_ACCOUNT", "PASSWORD")
        self.ID = config.get("NIKE_ACCOUNT", "ID")
        self.card = config.get("CREDIT_CARD", "CCNUM")
        self.ccsecurity = config.get("CREDIT_CARD", "CCV")
        self.expiration_month = config.get("CREDIT_CARD", "EXPM")
        self.expiration_year = config.get("CREDIT_CARD", "EXPY")



    def land_item_page(self) -> None:
        '''Open item page'''
        self.get(const.ITEM_URL)
        randomWaitTime = random.randrange(1, 3)
        time.sleep(randomWaitTime)

    def login(self) -> None:
        '''Navigate to log in page and submit credentials'''
        self._nav_login()
        action = ActionChains(super())

        loginFieldElement = self.find_element(By.XPATH, const.EMAIL_FIELD_XPATH)
        passwordFieldElement = self.find_element(By.XPATH, const.PASSWORD_FIELD_XPATH)
        submitSignInButtonElement = self.find_element(By.XPATH, const.SUBMIT_SIGN_IN_BUTTON_XPATH)

        action.move_to_element(loginFieldElement)
        action.click(loginFieldElement)
        action.perform()
        self._send_keys_delayed(self.username, loginFieldElement, action)
        randomWaitTime = random.uniform(0.2, 0.7)
        time.sleep(randomWaitTime)

        action.move_to_element(passwordFieldElement)
        action.click(passwordFieldElement)
        action.perform()
        self._send_keys_delayed(self.password, passwordFieldElement, action)
        randomWaitTime = random.uniform(0.2, 0.7)
        time.sleep(randomWaitTime)

        submitSignInButtonElement.click()


    def purchase(self) -> None:
        '''Execute a purchase'''
        self._select_color()
        self._select_size()
        self._add_to_cart()
        self._checkout()

    def _send_keys_delayed(self, word:str, element, action) -> None:

        for character in word:
            randomWaitTime = random.uniform(0.05, 0.13)
            action.send_keys(character)
            action.perform()
            time.sleep(randomWaitTime)


    def _checkout(self) -> None:
        '''Uses the webdriver to complete order'''
        cartButtonElement = self.find_element(By.XPATH, const.CART_BUTTON_XPATH)
        cartButtonElement.click()
        randomWaitTime = random.randrange(1, 3)
        time.sleep(randomWaitTime)
        checkoutButtonElement = self.find_element(By.XPATH, const.CHECKOUT_BUTTON_XPATH)
        checkoutButtonElement.click()
        randomWaitTime = random.randrange(1, 3)
        time.sleep(randomWaitTime)
        placeOrderButtonElement = self.find_element(By.XPATH, const.PLACE_ORDER_BUTTON_XPATH)
        placeOrderButtonElement.click()

    def _select_color(self) -> None:
        '''Uses the webdriver to select the color of item to be checked out'''
        colorButtonElement = self.find_element(By.XPATH, const.COLOR_BUTTON_XPATH)
        colorButtonElement.click()

    def _select_size(self) -> None:
        '''Uses the webdriver to select the size of item to be checked out'''
        sizeButtonElement = self.find_element(By.XPATH, const.SIZE_BUTTON_XPATH)
        sizeButtonElement.click()

    def _add_to_cart(self) -> None:
        '''uses the webdriver to add item to cart'''
        addToCartElement = self.find_element(By.XPATH, const.ADD_TO_BAG_BUTTON_XPATH)
        addToCartElement.click()

    def _nav_login(self) -> None:
        '''Locate login button element and clicking on it'''
        signInButtonElement = self.find_element(By.XPATH, const.SIGN_IN_BUTTON_XPATH)
        signInButtonElement.click()

     