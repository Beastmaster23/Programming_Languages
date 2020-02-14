from Employee import*
from Manager import*

emp= Employee("Julia", 200000)

print("Employee %s pay %.2f"% (emp.getFormattedName() ,emp.calculatePay()))
emp= Employee("Anna", 200000, exempt=2)

print("Employee %s pay %.2f"% (emp.getFormattedName() ,emp.calculatePay()))
man=Manager("Hhhm", 10000000, 10000, "BeastMaster")
print("Manager %s pay %.2f"% (man.getFormattedName() ,man.calculatePay()))

