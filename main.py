from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

EMAIL = os.environ.get('EMAIL')
ITALKI_PASSWORD = os.environ.get('ITALKI_PASSWORD')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
PAYPAL_PASSWORD = os.environ.get('PAYPAL_PASSWORD')
CHROME_PATH = os.environ.get('CHROME_PATH')
MINIMUM_MONEY_TO_WITHDRAW = 200


class Bot:

    def __init__(self):
        self.current_money_to_withdraw = 0
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        self.titles = []
        self.type_of_withdrawal = None

    # Italki Section

    def login_to_italki(self):

        self.driver.get('https://teach.italki.com/')

        time.sleep(8)
        login_button = self.driver.find_element_by_xpath('//*[@id="header_container"]/div/div/div[1]/span')
        login_button.click()

        time.sleep(2)
        email_input = self.driver.find_element_by_xpath('//*[@id="signinForm_email"]')
        email_input.send_keys(EMAIL)

        time.sleep(2)
        password_input = self.driver.find_element_by_xpath('//*[@id="signinForm_password"]')
        password_input.send_keys(ITALKI_PASSWORD)

        time.sleep(2)
        submit_button = self.driver.find_element_by_xpath('//*[@id="signinForm"]/div[4]/div/div/div/div/button')
        submit_button.click()

    def get_number_of_money(self):
        time.sleep(10)
        prices_elements = self.driver.find_elements_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div[1]/div/div[2]/div[2]/div')
        for item in prices_elements:
            self.current_money_to_withdraw = float(item.text.split(' ')[1])
            return self.current_money_to_withdraw

    def compare_money(self):
        if self.current_money_to_withdraw < MINIMUM_MONEY_TO_WITHDRAW:
            money_difference = float(MINIMUM_MONEY_TO_WITHDRAW) - self.current_money_to_withdraw
            print(f'The transaction is not successful.\nYour current balance is {self.current_money_to_withdraw}\n'
                  f'You still need to earn {money_difference}')
            return False
        elif self.current_money_to_withdraw < 30:
            print('You cannot withdraw money, when you current balance is less than 30 dollars')
            return False
        else:
            return True

    def withdraw_money_from_italki(self):

        time.sleep(5)
        withdraw_button = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div[2]/div/div[1]/div/div[2]/div[3]/a/span')
        withdraw_button.click()

        time.sleep(3)
        amount_of_money_to_withdraw = self.driver.find_element_by_xpath(
            '//*[@id="modal-container"]/div[2]/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/input')
        amount_of_money_to_withdraw.send_keys(int(self.current_money_to_withdraw))

        self.type_of_withdrawal = input('How do you want to withdraw money - regular or express? ')

        if self.type_of_withdrawal == 'regular'.lower():

            time.sleep(3)
            platform_to_withdraw = self.driver.find_element_by_xpath(
                '//*[@id="modal-container"]/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div[1]/span')
            platform_to_withdraw.click()

            time.sleep(3)
            next_button = self.driver.find_element_by_xpath('//*[@id="modal-container"]/div[2]/div/div[3]/button/span')
            next_button.click()

            time.sleep(3)
            agree_checkbox = self.driver.find_element_by_xpath(
                '//*[@id="modal-container"]/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/label/span[1]/input')
            agree_checkbox.click()

            time.sleep(3)
            password_input = self.driver.find_element_by_xpath(
                '//*[@id="modal-container"]/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div[2]/input')
            password_input.send_keys(ITALKI_PASSWORD)

            send_money_button = self.driver.find_element_by_xpath(
                '//*[@id="modal-container"]/div[2]/div/div[3]/button/span')
            send_money_button.click()

            return self.type_of_withdrawal

        elif self.type_of_withdrawal == 'express'.lower():

            time.sleep(3)
            platform_to_withdraw = self.driver.find_element_by_xpath(
                '//*[@id="modal-container"]/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div[1]/span')
            platform_to_withdraw.click()

            time.sleep(2)
            express_button = self.driver.find_element_by_xpath('//*[@id="modal-container"]/div[2]/div/div[2]/div/div['
                                                               '2]/div[1]/div[2]/div[2]/label[2]/span[1]/input')
            express_button.click()

            time.sleep(3)
            next_button = self.driver.find_element_by_xpath('//*[@id="modal-container"]/div[2]/div/div[3]/button/span')
            next_button.click()

            time.sleep(3)
            first_checkbox = self.driver.find_element_by_xpath(
                '//*[@id="modal-container"]/div[2]/div/div[2]/div/div/div[2]/div[2]/label/span[1]/input')
            first_checkbox.click()

            time.sleep(3)
            second_checkbox = self.driver.find_element_by_xpath(
                '//*[@id="modal-container"]/div[2]/div/div[2]/div/div/div[2]/div[3]/label/span[1]/input')
            second_checkbox.click()

            time.sleep(3)
            password_input = self.driver.find_element_by_xpath(
                '//*[@id="modal-container"]/div[2]/div/div[2]/div/div/div[3]/div[2]/input')
            password_input.send_keys(ITALKI_PASSWORD)

            time.sleep(3)
            send_money_button = self.driver.find_element_by_xpath(
                '//*[@id="modal-container"]/div[2]/div/div[3]/button/span')
            send_money_button.click()

            return self.type_of_withdrawal

    # Email section

    def login_to_mail(self):

        self.driver.get('https://mail.ru/')

        time.sleep(2)
        email = self.driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/div[1]/div[2]/input')
        email.send_keys(EMAIL)

        time.sleep(2)
        next_button = self.driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/button[1]')
        next_button.click()

        time.sleep(2)
        password = self.driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/div[2]/input')
        password.send_keys(EMAIL_PASSWORD)

        time.sleep(2)
        login_button = self.driver.find_element_by_xpath('//*[@id="mailbox"]/form[1]/button[2]')
        login_button.click()

    def parse_unread_messages(self):

        time.sleep(3)
        filter_button = self.driver.find_element_by_xpath(
            '//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[1]/span/div[2]/table/tbody/tr/td[2]/div/div/div/div/div['
            '1]/div/div[1]/span/span')
        filter_button.click()

        time.sleep(2)
        filter_messages = self.driver.find_element_by_xpath(
            '//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[1]/span/div[2]/table/tbody/tr/td[2]/div/div/div/div/div['
            '2]/div/div[2]/span[2]')
        filter_messages.click()

        time.sleep(2)
        unread_messages = self.driver.find_elements_by_class_name('ll-crpt')
        for message in unread_messages:
            self.titles.append(message.text)
        if 'service@paypal.com' in self.titles:
            print('Payment has been received. Going to withdraw from PayPal')
            return True
        elif 'service@paypal.com' not in self.titles:
            print('Payment has not been received yet')
            return False

    # Paypal Section

    def login_to_paypal(self):

        self.driver.get('https://www.paypal.com/ru/signin')

        mail_input = self.driver.find_element_by_xpath('//*[@id="email"]')
        mail_input.send_keys(EMAIL)
        mail_input.send_keys(Keys.ENTER)

        time.sleep(2)
        password_input = self.driver.find_element_by_xpath('//*[@id="password"]')
        password_input.send_keys(PAYPAL_PASSWORD)

        time.sleep(10)
        password_input.send_keys(Keys.ENTER)

    def withdraw_money_from_paypal(self):

        time.sleep(2)
        withdraw_money_button = self.driver.find_element_by_xpath('//*[@id="A"]/div/div[2]/div/div[3]/a')
        withdraw_money_button.click()

        time.sleep(3)
        ratio_button = self.driver.find_element_by_xpath('//*[@id="mainModal"]/div/div/div/div/div/div/ul/li/div/label')
        ratio_button.click()

        time.sleep(3)
        next_button = self.driver.find_element_by_xpath('//*[@id="mainModal"]/div/div/div/div/div/button')
        next_button.click()

        time.sleep(2)
        submit_withdrawing_money = self.driver.find_element_by_xpath('//*[@id="mainModal"]/div/div/div/form/button')
        submit_withdrawing_money.click()

        time.sleep(3)
        check_and_confirm_button = self.driver.find_element_by_xpath(
            '//*[@id="mainModal"]/div/div/div/form/div[4]/button')
        check_and_confirm_button.click()

        time.sleep(3)


bot = Bot()
bot.login_to_italki()
bot.get_number_of_money()
if bot.compare_money():
    bot.withdraw_money_from_italki()
    bot.login_to_mail()
    while not bot.parse_unread_messages():
        if bot.type_of_withdrawal == 'express'.lower():
            time.sleep(900)
        elif bot.type_of_withdrawal == 'regular'.lower():
            time.sleep(3600)
    bot.login_to_paypal()
    bot.withdraw_money_from_paypal()
    bot.driver.quit()
