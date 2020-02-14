from BankAccount import*
from Bank import*
from Employee import*
from Manager import*

bank = Bank("Interco Bank", 500)
(interco, bankId, intercoCash) = bank.createBankAccount("Interco", 20000000)
man = Manager("Hhhm", 10000000, 10000, "BeastMaster")
print("Manager %s pay %.2f" % (man.getFormattedName(), man.calculatePay()))
(name, bankId, cash) = bank.createBankAccount(man.getFormattedName(), 200000)
print("%s account %.2f" % (name, cash))
try:
    bank.transfer(bank.accounts[interco],
                 bank.accounts[name], man.calculatePay())
    print("%s account %.2f" % (name, bank.accounts[name].cash))
except InsufficientFundsError:
    print("We can't pay you :(")
    print("%s account %.2f" % (interco, bank.accounts[interco].cash))
print("%s transactions %s" % (name, bank.transactions[name].print()))
emp = Employee("Julia", 200000)
print("Employee %s pay %.2f" % (emp.getFormattedName(), emp.calculatePay()))
(name, bankId, cash) = bank.createBankAccount(emp.getFormattedName(), 20000)
print("%s account %.2f" % (name, cash))
try:
    bank.transfer(bank.accounts[interco],
                 bank.accounts[name], emp.calculatePay())
    print("%s account %.2f" % (name, bank.accounts[name].cash))
except InsufficientFundsError:
    print("We are broke :(")
    print("%s account %.2f" % (interco, bank.accounts[interco].cash))

bank.withdraw(bank.accounts[name], 6000)
bank.withdraw(bank.accounts[name], 3000)

print("%s transactions %s" % (name, bank.transactions[name].print()))

print("%s transactions %s" % (interco, bank.transactions[interco].print()))
