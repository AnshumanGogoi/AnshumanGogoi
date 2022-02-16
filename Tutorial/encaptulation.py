""" What is Encapsulation?
When working with classes and dealing with sensitive data, providing global access to all the variables
used within the program is not a good choice. Encapsulation offers a way for us to access the required variables
without providing the program full-fledged access to any of those variables."""



""" Using Getter and Setter methods to access private variables
If you want to access and change the private variables, accessor (getter) methods
and mutators(setter methods) should be used, as they are part of Class.
"""


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def display(self):
        print(self.name)
        print(self.__age)

    def getAge(self):
        print(self.__age)

    def setAge(self, age):
        self.__age = age


person = Person('Dev', 30)
# accessing using class method
person.display()
# changing age using setter
person.setAge(35)
person.getAge()
