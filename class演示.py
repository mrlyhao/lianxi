class Human(object):
    def __init__(self,name):
        self.names = name
    def walk(self):
        print (self.names + "is walking")

human_a = Human("alan")
human_a.walk()
print (human_a.names)