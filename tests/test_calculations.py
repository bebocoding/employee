import pytest
from app.calculations import *


@pytest.fixture
def zero_bank_account():
    print("Creating empty bank acoount")
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(6000)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (6, 3, 9)
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected


def test_subtract():
    assert subtract(6, 2) == 4


def test_multiply():
    assert multiply(5, 2) == 10


def test_divide():
    assert divide(6, 2) == 3


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 6000


def test_bank_default_amount(zero_bank_account):
    print("testing empty bank account")
    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):
    bank_account.withdraw(1000)
    assert bank_account.balance == 5000


def test_deposite(bank_account):
    bank_account.deposite(200)
    assert bank_account.balance == 6200


def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 6600


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (500, 100, 400),
    (50, 10, 40),
    (1200, 200, 1000)

])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposite(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(7000)
