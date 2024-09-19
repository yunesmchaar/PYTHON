
#This is my first Python program

print("I like pizza!")
print("It's really good!")

# variable = A container for a value (string,integer, float,boolean)
#A variable behaves as if it was the value it contains
#String
first_name = "YUNESS"
food="pizza"
email= "yunes.mchaar@gmail.com"
#Integers
age = 25
quantity = 3
num_of_students = 30

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is:{email}")
print(f"You are :{age}")
print(f"You are:{quantity} items")
print(f"Your class has {num_of_students} students")

# float

price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is {price}$")
print(f"Your gpa is: {gpa}")
print(f"Your distance is:{distance}km")


#Boolean

is_student = False
print(f"Are you a student?:{is_student}")
if is_student:
    print("you are a student")
else:
    print("You are Not a student")
for_sale = True
if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")
is_online= False
if is_online:
    print(f"You are online")
else:
    print(f"You are offline")

#typecasting = the process of converting a variable from one type to another
#str(),int(),float(),bool()

name="Bro Code"
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#afficher le contenue de age
age=str(age)
print(age)
print(type(age))

#input() = A function that prompts the user to enter data
#          Returns the entered data as a string

name=input("what is your name?:")
age=input("what is rour age?:")
age=int(age)
age+=1
print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age}!")

#Exercise 1 Rectangle Area Calc
length = input("Enter the length:")
width= input("Enter the width:")
length=int(length)
width=int(width)

area=length*width

print(f"The area is: {area}cm²")

#Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input ("What is the price?:"))
quantity = int(input("How many would you like?:"))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: {total}$")


















