#class Employee():
#    def employeeDetails(self):
#        self.name = 'Ben'
#    
#    @staticmethod
#    def welcomeMessage():
#        print('Welcome to our organization!')
### Static method = method without using self
#
#employee = Employee()
#employee.employeeDetails()
#print(employee.name)
#employee.welcomeMessage()

class Employee():
    def __init__(self,name):
        self.name = name
    
#    def __init__(self):
#        self.name = 'Mark'    

#        def enterEmployeeDetails(self):
#        self.name = name
    
    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee('mark')
employee.displayEmployeeDetails()