#Basicx function 
def greet_user(name):
    print(f"Welcome, {name}")

greet_user("Deepak")
print("--------------------------")   

#Return function

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("Sum:", result)
print("--------------------------")   

#Defualt argument

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Luna", "cat")
describe_pet("Rocky")
print("--------------------------")   

#using args
def sum_all(*args):
    return sum(args)

total = sum_all(1, 2, 3, 4, 5)
print("Total Sum:", total)
print("--------------------------")   

#using kwargs

def build_profile(first_name, last_name, **kwargs):
    profile = {
        "first_name": first_name,
        "last_name": last_name
    }
    profile.update(kwargs)
    print(profile)

build_profile("Deepak", "Rajesh", location="Kerala", job="Developer")
print("--------------------------")   

#scope
count=0
def update_count():
    global count  
    count += 1
    print("Updated Count:", count)

update_count()


# Explanation:
# Without 'global', Python treats count as a local variable inside the function . causing an error if we try count += 1 .
# Using 'global count' tells Python to use the global variable instead and it allow to update the count.