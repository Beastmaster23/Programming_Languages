from BankAccount import*

class Person(BankAccount):
    def __init__(self, name, bankId, cash):
        super().__init__(name, bankId, cash)
        