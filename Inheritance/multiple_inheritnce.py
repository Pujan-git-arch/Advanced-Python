class Father:
    def __init__(self):
        self.father_name = "John"

    def show_father(self):
        print("Father:", self.father_name)

class Mother:
    def __init__(self):
        self.mother_name = "Jane"

    def show_mother(self):
        print("Mother:", self.mother_name)
        
class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self) # Initialize Father's attributes #if not done, it will not call the Father class constructor
        Mother.__init__(self) # Initialize Mother's attributes #if not done, it will not call the Mother class constructor 
        self.child_name = "Alice"

    def show_child(self):
        print("Child:", self.child_name)
        Father.show_father(self) # Call Father's method # we cannot use super() here because we have multiple inheritance, so we need to call the parent class method directly #also we couldnot have used this if we hadnot called the parent class constructor
        Mother.show_mother(self) # Call Mother's method # we couldnot have used this if we hadnot called the parent class constructor i.e. if we hadnot called the parent class constructor, we would not have been able to access the parent class attributes and methods
        
child = Child()
child.show_child()