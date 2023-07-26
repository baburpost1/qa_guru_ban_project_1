from selene.support.shared import browser
from selene import be, have


def test_selene(open_google):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_check_empty_request(open_google):
    browser.element('[name="q"]').should(be.blank).type('35353nv345cdf!!fsdfs').press_enter()
    browser.element("[class='LHJvCe'] [id='result-stats']").should(have.text('Результатов: примерно 0'))
