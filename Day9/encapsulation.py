# Student Class
class Student:
    name = "ABC"  

    def __init__(self, name, id_number):
        self.name = name              
        self.__id_number = id_number  

    # Getter
    def get_id(self):
        return self.__id_number

    # Setter
    def set_id(self, new_id):
        if len(str(new_id)) == 4:
            self.__id_number = new_id
            print("ID updated successfully")
        else:
            print("Invalid ID (must be 4 digits)")

    # Instance method
    def study(self, subject):
        print(f"{self.name} is studying {subject}")

    # Class method
    @classmethod
    def school_info(cls):
        print(f"School Name: {cls.name}")



student1 = Student("Deepak", 1261)

print("Name:", student1.name)
# print(student1.__id_number)

print("ID (using getter):", student1.get_id())

# Update ID using setter
student1.set_id(5998)
print("Updated ID:", student1.get_id())

# Invalid update
student1.set_id(62)

# Instance method
student1.study("Python")

# Class method
Student.school_info()