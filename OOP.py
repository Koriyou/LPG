# Everything is an object in python

class Dog(object):
    def __init__(self,name): #initializes the class when object is defined things inside self are like variables
        self.name = name #this is the attribute to be filled when dog is created
        print('nice you made a dog')
    def speak(self): # this is called a method
        print('hi i am',self.name)

class Cat(Dog):
    def __init__(self, name, color):
        super().__init__(name)
        self.color= color

tim = Dog('Tim') #this will initialize the object and create an instances of it and it's attributes
tim.speak() # this calls the method inside the object tim