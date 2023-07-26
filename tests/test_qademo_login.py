from selene import browser, have, be
from selene.core import configuration

user_name = 'Pussy destroyer'
user_email = 'pssdest@ban.com'
user_current_adress = 'улица пушкина'
user_permanent_adress = 'Дом колотушкина'

input_name = '[ id="userName"]'
input_email = '[id="userEmail"]'
input_current_adress = '[id="currentAddress"]'
input_permanent_address = '[id="permanentAddress"]'
button_submit = '[id="submit"]'


def test_signup_user():
    browser.open('https://demoqa.com/text-box')
    browser.element()
    browser.element(input_name).should(be.blank).type(user_name).press_tab()
    browser.element(input_email).should(be.blank).type(user_email).press_tab()
    browser.element(input_current_adress).should(be.blank).type(user_current_adress).press_tab()
    browser.element(input_permanent_address).should(be.blank).type(user_permanent_adress)
    browser.element(button_submit).click()
    browser.element('[id="name"]').should(have.exact_text(f'Name:{user_name}'))

