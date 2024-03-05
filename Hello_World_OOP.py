
class Person():
    def __init__(self,forename,age=None,surname=None,title=None,occupation=None):
        self.forename = forename
        self.surname = surname
        self.title = title
        self.occupation = occupation
        self.age = age
    
    def hello(self):
        print("Hello, my name is %s." % self.forename)
    
    def say_full_name(self):
        print("My full name is %s %s %s." % (self.title,self.forename,self.surname))
    
    def occupation(self):
        print("I'm a %s." % (self.occupation))
    
    def full_list(self):
        print("Forename:%s" % self.forename)
        print("Surname:%s" % self.surname)
        print("Title:%s" % self.title)
        print("Occupation:%s" % self.occupation)
        print("Age:%s" % self.age)

person_1 = Person(forename="Cameron")

person_1.age = "25"
person_1.surname = "Cochrane"
person_1.title = "Mr"
person_1.occupation = "Student"

person_1.full_list()

    



        