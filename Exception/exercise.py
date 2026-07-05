
# Exercise: Raise Exception And Finally
# Create a custom exception AdultException.

# Create a class Person with attributes name and age in it.

# Create a function get_minor_age() in the class. It throws an exception if the person is adult otherwise returns age.

# Create a function display_person() which prints the age and name of a person.

# let us say,

# if age>18 
#     he is major
# else
#     raise exception

# create cusomException named ismajor and raise it if age<18.

class AdultException(Exception):
    def __init__(self,message):
        self.message = message
        
    def print_exception(self):
        print("Userdefined Exception: ",self.message)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def get_minor_age(self):
        if self.age > 18:
            raise AdultException("Person is an adult, not a minor")
        else:
            print(f"{self.name} is a minor. with age {self.age}")
    
    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
Person1 = Person("John", 20)
try:
    Person1.get_minor_age() 
except AdultException as e:
    e.print_exception()
    
    