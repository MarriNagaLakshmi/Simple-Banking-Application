from app import BankingApp

def test_bank():
    app = BankingApp()
    app.deposit(200)
    assert "Withdrew $300" in app.withdraw(300)
    assert app.balance == 900.0
    assert "Insufficient funds" in app.withdraw(5000)
