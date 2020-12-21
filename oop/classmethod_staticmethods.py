#class method and static methods in python


class Employee:
    #class varible for upgrading the pay
    raise_amount = 1.04
    #number of the employee
    num_of_emp = 0

    #___init__ method
    #we are incrementing the employee number in here since this method is called when ever a new employee is created
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"
        Employee.num_of_emp += 1

    #full name method
    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

    #function common to all the class object
    #self will help in overriding the default class variable value
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  #increase the pay by 5%


#creating an employee object
emp1 = Employee("testname", "lasttestname", 60000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)  #notice the change in pay value
'''
when we are trying to access the class variable the first it checks if the 
variable is present in the object we are refering to and if it is not present in the
object that we pass in to the class method then it searches the super class from which it
is inherited !!
'''

#accessing the name space of employee 1 (emp1)
#we can update the raise_amount attribute the emp1 using its own attribute
print(emp1.__dict__)  #this will not have the raise amount class variable

#accessing the name space fo the employee class
print(Employee.__dict__
      )  #now this will have the raise amount class variable listed in it
