# Object-Oriented Programming
# If you want to build an object you need a class (the design - the blueprint)

class Computer:
    # Attributes empty at the moment
    # Behaviour - Methods
    def config(self):
        print("i5, 16GB, 1TB")


com1 = Computer()
print(type(com1))
print(type("test"))
print(type(8))
# everything is object in Python
com1.config()

a = 5
a.bit_length()

# The __init__ method - special method


class Computer:

    def __init__(self, cpu, ram):
        print("In __init__")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is: {0} CPU and {1} GB RAM".format(self.cpu, self.ram))


com1 = Computer("i5", 16)
com1.config()

com2 = Computer("Ryzen 3", 8)
com2.config()

# Constructor, Self and Comparing Objects


class Computer:

    def __init__(self):
        self.name = "Alan"
        self.age = 27

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False



c1 = Computer()
c1.update()
print(id(c1))

c2 = Computer()
print(id(c2))

if c1.compare(c2):
    print("They are the same")


class Car:
    # Outside of __init__ you define class variables, within __init__ you define instance variables
    wheels = 4

    def __init__(self):
        self.mileage = 10
        self.company = "Chal-Tec"


car1 = Car()
car2 = Car()
car1.company = "Pappa Beach"
car2.wheels = 5

print(car1.mileage, car1.company, car1.wheels)
print(car2.mileage, car2.company, car2.wheels)

car1.company = "Pappa Beach"
car2.wheels = 5

print(car1.mileage, car1.company, car1.wheels)
print(car2.mileage, car2.company, car2.wheels)

Car.wheels = 6

print(car1.mileage, car1.company, car1.wheels)
print(car2.mileage, car2.company, car2.wheels)

# Types of Methods


class Student:

    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class")



s1 = Student(40, 50, 60)
s2 = Student(20, 100, 70)
print(s1.avg())
print(s2.avg())
print(s1.get_m1())
s1.set_m1(35)
print(s1.get_m1())
print(Student.getSchool())
print(Student.info())

# Inner Class
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 32


s1 = Student("Alan", 3)
s1 = Student("Jenny", 10)
print(s1.name, s1.rollno)
s1.show()
print(s1.lap.brand)
print(s1.lap.ram)

# Inheritance
class A:
    def feature1(self):
        print("Feature 1 is working!")

    def feature2(self):
        print("Feature 2 is working!")


class B(A):
    def feature3(self):
        print("Feature 3 is working!")

    def feature4(self):
        print("Feature 4 is working!")


class C(B):
    def feature5(self):
        print("Feature 5 is working")


a1 = A()
a2 = A()
a1.feature1()
a2.feature2()

b1 = B()
b2 = B()
b1.feature3()
b2.feature4()
b1.feature1()

c1 = C()
c1.feature1()
c1.feature5()

# Constructor in Inheritance
class A:

    def __init__(self):
        print("In A __init__")

    def feature1(self):
        print("Feature 1 is working!")

    def feature2(self):
        print("Feature 2 is working!")


class B(A):

    def __init__(self):
        super().__init__()
        print("In B __init__")

    def feature3(self):
        print("Feature 3 is working!")

    def feature4(self):
        print("Feature 4 is working!")

a1 = A()
a1.feature1()
b1 = B()
b1.feature2()


# Polymorphism
# Duck Typing
x = 5
print(id(x))
x = " Alan"
print(id(x))


class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running!")


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Compiling")
        print("Running!")


class Laptop:

    def code(self, ide):
        ide.execute()


ide = PyCharm()
ide2 = MyEditor()

lap1 = Laptop()
lap1.code(ide)
lap1.code(ide2)

# Operator OverLoading
a = 5
b = 6
print(a+b)
print(int.__add__(a, b))


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2

        if m1 > m2:
            return True
        else:
            return False


s1 = Student(60, 80)
s2 = Student(90, 100)

s3 = s1 + s2
print(s3.m1)

if s1 > s2:
    print("s1 is better student")
else:
    print("s2 is equal or better to s1")
















