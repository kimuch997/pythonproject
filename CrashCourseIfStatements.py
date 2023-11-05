cars = ["audi","bmw","toyota","range","forester"]
for car in cars:
    if car == 'bmw':
        # == equality operator checks whether the value of the right and left side is true
        print(car.upper())
    else:
        print(car.title())

car = 'audi'
car = 'Audi'
# False

car = 'Audi'
# car.lower() = 'audi'
# TRUE

# The lower() function doesn’t change
# the value that was originally stored in car, so you can do this kind of comparison
# without affecting the original variable:

# Websites enforce certain rules for the data that users enter in a
# manner similar to this. For example, a site might use a conditional test
# like this to ensure that every user has a truly unique username, not just a
# variation on the capitalization of another person’s username. When someone submits a new username, that new username is converted to lowercase
# and compared to the lowercase versions of all existing usernames. During
# this check, a username like 'John' will be rejected if any variation of 'john'
# is already in use.


requested_topping = 'muhsrooms'
if requested_topping != "anchovies":
    print("Hold the mushrooms.")
#     testing for inequality
#     =!(not equal) determines if the two values match and if they do not match the if statement is executed if they do match the if statement is not executed
answer = 17
if answer != 42:
    print("Hold up that is not the correct answer.")

# and both conditions have to be true

age = 19
if age < 20 and age >= 89 :
    print("Definately true.")
else:
    print("false")

#     or only one condition has to be true
life = 45
if life >= 67 or life <= 56:
    print('true')
else:
    print("False.")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
print("Yes it is in requested topings.")

'pineapple' in requested_toppings
print("No it is not in requested topings.")

# Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(f"{user.title()}, you can post a response if you wish.")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


life_expectancy = 60
if life_expectancy == 20  or life_expectancy != 20:
    print("True")
else:
    print("THE ABOVE WAS NOT CORRECT")


funcky_list = ["fidel","jere","anto","samuel"]

player = "fidel"
if player not in funcky_list:
    print("fidel your not in the list,izzah bro")
else:
    print("acha kutense uko kwa list")

