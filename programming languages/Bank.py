from BankAccount import*
from Stack import*
class BankDepositError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class InsufficientFundsError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Bank:

    def __init__(self, name, cash, currency="US", maxHistory=5):
        self.name=name
        self.currency=currency
        self.maxHistory=maxHistory
        self.transactions={}
        self.accounts={}
    
    def createBankAccount(self, name, cash=0):
        self.accounts[name]=BankAccount(name, self.name, cash)
        self.transactions[name]=Stack()
        return (name, self.accounts[name].bankId, cash)
    def addTransaction(self, fromAcount, toAccount, amount):
        self.transactions[fromAcount.name].push((fromAcount.name, toAccount.name, amount))
    def transfer(self, fromAcount, toAccount, amount=0):
        if fromAcount.cash-amount>=0:
            toAccount.cash+=amount
            fromAcount.cash-=amount
            self.addTransaction(fromAcount, toAccount, -amount)

        else :
            raise InsufficientFundsError("Insufficient funds...")

    def withdraw(self, acount, amount=0):
        if acount.cash-amount>=0:
            acount.cash-=amount
            self.addTransaction(acount, acount, -amount)
        else :
            raise InsufficientFundsError("Insufficient funds...")