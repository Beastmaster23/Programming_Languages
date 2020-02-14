from Employee import*
class Manager(Employee):
    def __init__(self, name, salary, bonus, prefix="", exempt=1):
        self.bonus=bonus
        super().__init__(name, salary, prefix, exempt)
    
    def calculatePay(self):
        return super().calculatePay()+self.bonus/12