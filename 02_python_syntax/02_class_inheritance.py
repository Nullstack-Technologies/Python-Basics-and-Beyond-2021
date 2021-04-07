class Person:
    name = ""
    age = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person<{self.name}>"

    def __eq__(self, value):
        return self.age == value.age

    def __lt__(self, value):
        return self.age < value.age

    def full_name(self):
        return f"{self.name} | {self.age} yrs"


class Teacher(Person):
    qualification = ""
    years_of_experience = ""

    def __init__(self, name, age, qualification, years_of_experience):
        super().__init__(name, age)
        self.qualification = qualification
        self.years_of_experience = years_of_experience

    def __str__(self):
        full_name = super().full_name()
        return f"Teacher {full_name} | Qualification {self.qualification}"


teacher_1 = Teacher("John", 36, "MS", 12)
print(teacher_1)



class Vehicle:
    """
        Vehicle is a device 
    """

    wheels = 0

    def ignition(self):
        pass

    def braking(self):
        pass

    def __init__(self):
        super().__init__()


class Car(Vehicle):

    wheels = 4


