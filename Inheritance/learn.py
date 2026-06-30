# Parent Class
class Vehicle:

    # Common method inherited by all child classes
    def general_usage(self):
        print("General Use: Transportation")


# Child Class - Car
class Car(Vehicle):

    def __init__(self):
        print("I am Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Specific Usage: Commute to work, Vacation with family")


# Child Class - Bike
class Bike(Vehicle):

    def __init__(self):
        print("I am Bike")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("Specific Usage: Road trip, Racing")


# Main Program
if __name__ == "__main__":

    # Create objects
    c = Car()
    b = Bike()

    # Store all objects inside a list
    vehicles = [c, b]

    # Ask user for the vehicle
    choice = input("\nWhich vehicle do you want? (car/bike): ").lower()

    # --------------------------------------------------------
    # BASIC METHOD (Using if-elif)
    #
    # if choice == "car":
    #     c = Car()
    #     print(f"I have {c.wheels} wheels")
    #
    #     if c.has_roof:
    #         print("I have roof")
    #     else:
    #         print("I don't have roof")
    #
    #     c.general_usage()
    #     c.specific_usage()
    #
    # elif choice == "bike":
    #     b = Bike()
    #     print(f"I have {b.wheels} wheels")
    #
    #     if b.has_roof:
    #         print("I have roof")
    #     else:
    #         print("I don't have roof")
    #
    #     b.general_usage()
    #     b.specific_usage()
    #
    # else:
    #     print("Invalid vehicle")
    # --------------------------------------------------------

    # POLYMORPHISM METHOD (Using for loop)
    for item in vehicles:

        # item.__class__.__name__ returns:
        # Car()  -> "Car"
        # Bike() -> "Bike"
        #
        # .lower() converts them to:
        # "car" or "bike"

        if choice == item.__class__.__name__.lower():

            print(f"\nI have {item.wheels} wheels")

            if item.has_roof:
                print("I have roof")
            else:
                print("I don't have roof")

            # Calls method from Vehicle class
            item.general_usage()

            # Calls the correct method depending on the object
            item.specific_usage()

            # Exit loop after finding the correct vehicle
            break

    else:
        print("Invalid vehicle")