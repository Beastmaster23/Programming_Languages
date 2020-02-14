class BankAccount:
    lastId=0
    def __init__(self, name, bankId, cash=0):
        self.cash=cash
        self.name=name
        self.bankId=bankId
        self.id=BankAccount.generateId()
    
    @classmethod
    def generateId(cls):
        if BankAccount.lastId==0:
            BankAccount.lastId=111
        BankAccount.lastId+=1
        return BankAccount.lastId