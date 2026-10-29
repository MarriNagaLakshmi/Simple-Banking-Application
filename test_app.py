import pytest
from app import BankingApp

def test_initial_balance():
    app = BankingApp()
    assert app.balance == 1000.0

def test_check_balance():
    app = BankingApp()
    assert "1000.00" in app.check_balance()

def test_deposit():
    app = BankingApp()
    result = app.deposit(500)
    assert app.balance == 1500.0
    assert "Successfully deposited $500.00" in result

def test_invalid_deposit():
    app = BankingApp()
    result = app.deposit(-100)
    assert app.balance == 1000.0
    assert "Invalid deposit amount." in result
    
   
