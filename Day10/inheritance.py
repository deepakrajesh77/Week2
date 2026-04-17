class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email
    def login(self):
        print(f"user {self.username} logged in")

class Admin(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)  
        self.permissions = permissions
    def login(self):
          print(f"Admin {self.username} logged in with full acccess")
     # Specialized Method
    def delete_user(self):
        print(f"Admin {self.username} can delete users.")

user1 = User("Deepak", "deepak@gmail.com")
admin1 = Admin("deepak", "deepak@gmail.com", "all")
users = [user1, admin1]

for u in users:
    u.login()
print()

admin1.delete_user()

