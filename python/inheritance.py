class person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("id number is {}".format(self.idnumber))

class Employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)
    def details(self):
        print("My name is: {}".format(self.name))
        print("Idnumber: {}".format(self.idnumber))
        print("My salary is: {}".format(self.salary))
        print("Post:{}".format(self.post))


a=Employee("Salman",8725,50000,"intern")
a.display()
a.details()
