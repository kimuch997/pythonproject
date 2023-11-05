for number in range(3):
    print("attempt", number + 1 ,(number + 1) * "NEKEE")


print("-----------------")

for number in range(1,10,):
    print("Attempt",number,number * "nekee")

    print("------------")

successfull = False
for number in range(3):
    print("attempt")
    if successfull:
         print("successfull")
         break
else:
    print("attempted 3 times and failed")


    print("---------------------")
    #nested loops

    
    for x in range (5):
        for y in range(3):
            print(f"{x},{y}")


print("---------------------------")



#iterables
print(type(5))

print((range))

for x in "python":
    print(x)

print("---------------------")
count = 0
for number in range(1,10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")

print("-------------------")


#WHILE LOOPS
# name = input("enter your name:")
# if name == "":
#     print("you did not enter your name.")
# else:
#     print("hello {name}")
#
# email = input("enter your email address")

# print("-----------------------------")
 # if you want to continually prompt the user to input data


# name = input("Enter your name.")
# while name == "":
#      print("Please fill this field.")
#      name = input("Enter your name.")
#      print(f"hello {name}")
#

# food = input("enter a food you like(q to quit):")
# while not food == "q":
#     print(f"you like {food}")
#     food = input("enter another a food you like(q to quit):")
#

# num = int(input("input a no. between 1 and 10:\n "))
# while num < 1 or num >= 10:
#     print(f"{num} is not a number between 1-10")
#     num = int(input("input a no. between 1 and 10"))
# print(f"your number is  {num} ")


#FOR LOOPS
# credit_card = "1234-3434-34556-3222"
# for x in credit_card:
#     print(x)
#
# #skipping over
# for x in  range(1,20):
#     if x == 13:
#         continue
#     else:
#         print(x)
#

#IF STATEMENTS

age = int(input("Enter your age: "))

while age == "":
    print("please fill this field.")

if age > 1 or age <= 18:
    print("You are a minor.")
elif age < 0 or age == 0:
    print("not yet born")
elif age >= 100:
    print("You are a phenomena.")
else:
    print("You are 18 and above hence you can  sign up.")

response = input("Would you like some food? (Y/N) :")
if response == "Y":
    print("have some food")
else:
    print("No food for you.")



# name = input("Enter your name: ")
# if name == "":
#     print("Please fill out this field.")
#     name = input("Enter your name: ")
# else:
#     print(f"Hello {name}.")


# for_sale = False
# if for_sale:
#      print("This item is for sale.")
# else:
#      print("Not for sale.")

# online = False
# if online:
#     print("User is online.")
# else:
#     print("User is not online.")
#












