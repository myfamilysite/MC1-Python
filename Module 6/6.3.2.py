# Create a class called Student that encapsulates the following attributes: name, age, and grade

class Student:
    def __init__(self, name:str, age:int, grade:str, school:str):
        self.name = name          # Public attribute
        self.__age = age          # Private attribute
        self.__grade = grade      # Private attribute
        self._school = school     # Protected attribute

    # Getter and Setter for Age (Private)
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age.")

    # Getter and Setter for Grade (Private)
    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    # Getter for School (Protected)
    def get_school(self):
        return self._school

# Test my code
user = Student("John", 25, "A", "ABC High School")  # name, age, grade, school)

print (user.get_age())

print(user.get_grade())

print(user.get_school())

print(user.name)




