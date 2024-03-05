
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
    

person_1 = Person(forename="Cameron")

person_1.age = "25"

print(person_1.age)

    



        