#class method and static methods in python

#the regular method automatically takes in the instance of a class as the first arguement and we can override this


class Employee:
    #class varible for upgrading the pay
    raise_amount = 1.04
    #number of the employee
    num_of_emp = 0

    '''documentation string __doc__ 
        included using \''' docstring \'''
        * need to be indended accordinly or error occurs
    '''

    #___init__ method
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"
        Employee.num_of_emp += 1

    #full name method
    def fullname(self):
        return ('{} {}'.format(self.first, self.last))

   
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  #increase the pay by 5%


    #defining a class method 
    #we are setting the class as the first arguement of this method
    @classmethod 
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount#changing the class variable value

    #new classmethod for making employee from string
    @classmethod 
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)#returns a new employee object for the new values


    @staticmethod
    def is_workday(day):
        if(day.weekday()==5 or day.weekday()==6):
            return False
        else:
            return True



#creating an employee object
emp1 = Employee("testname", "lasttestname", 60000)

#changing the employee class's raise amount the value
Employee.set_raise_amt(1.04)

#seting an employee from a string of value
emp2_str='emp2first-emp2last-20000'
first,last,pay=emp2_str.split('-')
emp2=Employee(first,last,pay)

print(emp2.fullname())

#can create another class method for serving the same purpose
emp3_str='emp3first-emp3last-40000'
emp3=Employee.from_string(emp3_str)#creating the employee3 instance
print(emp3.fullname())


#using the new static method
import datetime
my_date=datetime.date(2000,10,11)

print(Employee.is_workday(my_date))