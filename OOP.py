# # # class Dog():
# # #     # CLASS OBJECT ATTRIBUTE
# # #     #SAME FOR ANY INSTANCE OF A CLASS
# # #     species = 'Mammal'
# # #     def __init__(self,breed ,name):
# # #         self.breed = breed
# # #         self.name = name
# # #         #Boolean
# # #     #Operations/Actions ---> Methods
# # #     def bark(self, number):
# # #         print(f'Woof! my name is {self.name}  and the number is {number}')
# # # my_dog = Dog('Lab','Sammy')


# # # print(my_dog.bark(10))


# # # class Circle():
# # #     pi = 3.14
    
# # #     def __init__(self, radius=1):
# # #         self.radius = radius
# # #         self.area = radius *radius* Circle.pi

# # #     def get_circumference(self):
# # #         return self.radius * self.pi * 2
    
# # # my_cicle = Circle(30)

# # # print(my_cicle.get_circumference())


# # class Animal():
# #     def __init__(self):
# #         print('Animal Created')
# #     def who_am_i(self):
# #         print('I am an Animal')
# #     def eat(self):
# #         print('i am eating')

# # class Dog(Animal):
# #     def __init__(self):
# #         Animal.__init__(self)
# #         print('Dog Created')
# #     def who_am_i(self):
# #         print('I am a dog')
# #     def bark(self):
# #         print('wolf!')

# # mydog = Dog()

# # mydog.bark()

# class Dog():
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         return self.name + ' says Woof!'
    
# class Cat():
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         return self.name + ' says Meow!'
    
# niko = Dog('niko')
# felix = Cat('felix')
# # for pet in [niko,felix]:
# #     print(type(pet))
# #     print(type(pet.speak()))

# def pet_speak(pet):
#     print(pet.speak())

# pet_speak(niko)
# pet_speak(felix)

# # print(niko.speak())
# # print(felix.speak())

# class Animal():
#     def __init__(self,name):
#         self.name = name
    
#     def speak(self):
#         raise NotImplementedError('SubClass must implement this abstract method')

# myanimal = Animal('fred')

# class Dog(Animal):
#     def speak(self):
#         return self.name + " says Woof!"
    
# class Cat(Animal):
#     def speak(self):
#         return self.name + " says Meow!"
    
# fido = Dog('fido')
# Isis = Cat('Isis')

# print(fido.speak())
# print(Isis.speak())

mylist = [1,2,3]
len(mylist)

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __len__(self):
        return self.pages
    def __del__(self):
        print('A book object has been deleted')

b = Book('Pyhon Rocks', 'Orlando ', 200)
print(b)