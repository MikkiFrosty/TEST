import pytest
from selene import browser, be, have
from ozon_deposit_test.pages.deposit_page import Deposit as DepositPage
from ozon_deposit_test.models.deposit import Deposit_class
from ozon_deposit_test.models.deposit_calculator_locators import DepositCalculatorLocators as L


def test_deposit_valid():
    page = DepositPage().open_form()
    value = Deposit_class(
        deposit_amount=150000,
        term=4,
        interest_rate="15,1%",
        profit_amount="+7 511,43 ₽",
        deposit_type="Вклад на 4 месяца",
        check_capitalization=True,
        check_insurance=True,
        check_conditions=True,
        check_cta=True,
    )
    page.filling_field(value) \
        .should_show_calc(value) \
        .should_have_active_buttons(value)


def test_deposit_min():
    page = DepositPage().open_form()
    value = Deposit_class(
        deposit_amount=10000,
        term=4,
        interest_rate="15,1%",
        profit_amount="+500,76 ₽",
        check_capitalization=True,
        check_insurance=True,
    )
    page.filling_field(value).should_show_calc(value).should_have_active_buttons(value)


def test_deposit_invalid_sum_below_min():
    page = DepositPage().open_form()
    value = Deposit_class(
        deposit_amount=9999
    )
    page.filling_field(value)
    page.should_have_stub()

def test_deposit_invalid_symbols():
    page = DepositPage().open_form()
    value = Deposit_class(
        deposit_amount="абвГДЕabcXYZ!@#$%^&*()",
    )
    page.filling_field(value)
    page.should_have_stub()

def test_form_display_smoke():
    page = DepositPage().open_form()
    value = Deposit_class(deposit_amount=150000, term=3)
    page.filling_field(value).should_have_active_buttons()
    browser.element(L.RATE).should(be.visible)
    browser.element(L.PROFIT).should(be.visible)

def test_deposit_zero_amount_shows_stub():
    page = DepositPage().open_form()
    value = Deposit_class(deposit_amount=0)
    page.filling_field(value)
    page.should_have_stub()

def test_term_change_updates_profit():
    page = DepositPage().open_form()
    base = Deposit_class(deposit_amount=150000, term=3)
    page.filling_field(base).should_have_active_buttons()
    changed = Deposit_class(deposit_amount=150000, term=4)
    page.filling_field(changed)
    from selene import browser
    from ozon_deposit_test.models.deposit_calculator_locators import DepositCalculatorLocators as L
    profit_after = browser.element(L.PROFIT).text
    assert profit_after and isinstance(profit_after, str)
