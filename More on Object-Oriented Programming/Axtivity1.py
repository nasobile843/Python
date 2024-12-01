class IOString():

    def __init__(self):
        self.strl = ""

    def get_String(self):
        self.strl =input("Enter String: ")

    def print_String(self):
        print("Result is:", self.strl.upper())

strl = IOString()

strl.get_String()
strl.print_String()


