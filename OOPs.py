# 1. Single Inheritance
# Using: One child class inherits one parent class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_person(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def show_student(self):
        self.show_person()
        print(f"Roll No: {self.roll_no}")

s = Student("Alice", 20, "S101")
s.show_student()


# 2. Multiple Inheritance
# Using: One child class inherits multiple parent classes

class Father:
    def father_skill(self):
        print("Father's Skill: Gardening")

class Mother:
    def mother_skill(self):
        print("Mother's Skill: Cooking")

class Child(Father, Mother):
    def child_skill(self):
        print("Child's Skill: Sports")

c = Child()
c.father_skill()
c.mother_skill()
c.child_skill()


# 3. Multilevel Inheritance
# Using: Grandparent → Parent → Child

class Grandparent:
    def property_gp(self):
        print("Grandparent's Farmhouse")

class Parent(Grandparent):
    def property_p(self):
        print("Parent's City House")

class Child1(Parent):
    def property_c(self):
        print("Child's Apartment")

obj = Child1()
obj.property_gp()
obj.property_p()
obj.property_c()


# 4. Hierarchical Inheritance
# Using: Multiple child classes inherit one parent class

class Animal:
    def info(self):
        print("I am an animal")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.info()
d.sound()

c.info()
c.sound()


# 5. Hybrid Inheritance
# Using: Combination of multiple + multilevel inheritance

class School:
    def func1(self):
        print("School info")

class Teacher(School):
    def func2(self):
        print("Teacher info")

class Staff:
    def func3(self):
        print("Staff info")

class Student1(Teacher, Staff):
    def func4(self):
        print("Student info")

s = Student1()

s.func1()
s.func2()
s.func3()
s.func4()


# 6. Method Overloading
# Using: Default arguments

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()

print("One number:", calc.add(10))
print("Two numbers:", calc.add(10, 20))
print("Three numbers:", calc.add(10, 20, 30))


# 7. Method Overloading using *args
# Using: Variable length arguments

class Shape:
    def area(self, *args):
        if len(args) == 1:
            print("Square Area:", args[0] ** 2)
        elif len(args) == 2:
            print("Rectangle Area:", args[0] * args[1])

s = Shape()

s.area(5)
s.area(5, 10)


# 8. Method Overriding
# Using: Child class overrides parent method

class Parent1:
    def show(self):
        print("Inside Parent Class")

class Child2(Parent1):
    def show(self):
        print("Inside Child Class (Overridden)")

c = Child2()
c.show()


# 9. Runtime Polymorphism
# Using: Same method name with different implementation

class Employee:
    def salary(self):
        print("Base Salary: $3000")

class Manager(Employee):
    def salary(self):
        print("Manager Salary: $3000 + Bonus $2000")

m = Manager()
m.salary()


# 10. Using super() Method
# Using: Calling parent class method from child class

class Parent2:
    def greet(self):
        print("Hello from Parent")

class Child3(Parent2):
    def greet(self):
        super().greet()
        print("Hello from Child")

obj = Child3()
obj.greet()
