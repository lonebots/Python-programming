#object oriented programming
#creating a class and making its instances
#initialize method
#class methods

class Employee:
    #special __init__method - constructor like function in python
    #its first arg should be self 
    #this method take in the arguements and initialise the attributes
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+"@company.com"


    #defining a class method
    #code reuse 
    #this also take in the self as a parmeter
    #refering the attribute with self makes it easy for the function to work for all the class objects
    def fullname(self):
        return('{} {}'.format(self.first,self.last))

#creating an employee object 
emp1=Employee("testname","lasttestname",60000)
print(emp1.fullname())#print the full name of the employee