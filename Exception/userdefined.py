class Accident(Exception):
    def __init__(self,message):
        self.message = message
    def print_exception(self):
        print("Userdefined Exception: ",self.message)

try:
    raise Accident("CArs just collided, taking a detour")
except Accident as e:
    e.print_exception()