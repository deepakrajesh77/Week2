# Define Class
class Course:
    
    # Constructor
    def __init__(self, name, price, seats):
        self.name = name
        self.price = price
        self.seats = seats



    # Instance Method
    def display_info(self):
        print(f"Course: {self.name} , cost ₹{self.price}")


    # Update Seats
    def enroll_student(self):
        if self.seats > 0:
            self.seats -= 1
            print(f"1 student enrolled in {self.name}")
        else:
            print(f"{self.name} is already full")



    # Status Logic
    def get_status(self):
        if self.seats > 0:
            return "ACTIVE"
        else:
            return "FULL"

# Create Objects
course1 = Course("Full Stack Masterclass", 9999,6)
course2 = Course("Generative AI & LLMs", 12999, 0)
course3 = Course("Advanced System Design", 10999, 2)



# Call display_info
course1.display_info()
course2.display_info()
course3.display_info()
print()

# Enroll Students
course1.enroll_student()
course2.enroll_student()
course3.enroll_student()
print()
# Show Status
print(course1.get_status())
print(course2.get_status())
print(course3.get_status())