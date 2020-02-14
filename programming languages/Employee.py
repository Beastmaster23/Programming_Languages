class Employee:
    lastId=0
    def __init__(self, name, salary, prefix="", exempt=1):
        self.prefix=prefix
        self.name=name
        self.salary=salary
        self.exemptions=exempt
        self.id=Employee.generateId()
    
    @classmethod
    def generateId(cls):
        if Employee.lastId==0:
            Employee.lastId=111
        Employee.lastId+=1
        return Employee.lastId

    def getFormattedName(self):
        formattedName=self.name
        if self.prefix!="":
            formattedName=self.prefix+" "+formattedName
        return formattedName
    
    def calculatePay(self):
        if self.exemptions==1:
            return self.salary/12
        else:
            return self.salary/12*.9