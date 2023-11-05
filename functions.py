def hello():
    print("Hi!")
    print("have a good day.")


hello()
print("-----------")
def hello(name):
    print("Hello " + name.upper() )

hello("Kimathi")

print("-----------")
def enter(first_name,second_name,thrid_name):
    print("Enter your name:  "+first_name.upper()
          +" "+second_name.upper()+" "+thrid_name.upper())

enter("anthony","kimathi","mutethia")


print("---------------------")

def hello (name,age) :
    print(f"Happy birthday to {name}.")
    print(f"you are {age} years old")

hello("kim",19)
hello("kibe",47)
hello("kinuthia",39 )

print("------------------")
def display_invoice(username,amount,due_date):
    print(f"hello {username}")
    print(f"your bill of ${amount} is {due_date}")

display_invoice("kim",200,"28th of june")
display_invoice("kinuthia",300,"01/02")

#RETURN FUNCTIONS

def subtract(x,y):
    z = x-y
    return z

print(subtract(2,6))

print("----------")
def create_name(first_name,second_name):
     first_name = first_name.capitalize()
     second_name = second_name.capitalize()
     return first_name + "" + second_name

fullname = create_name("anthony  ","kimathi")
print(fullname)

#default parameter value
def nation(country = "norway"):

    print("i am from " + country)

nation("sweden")
nation("denmar")
nation("kenya")
nation()

#passing a list as an argument
def type_of_food(fruits):
    for fruit in fruits:
        print(fruit)
fruits = ["apple", "banana", "cherry"]
type_of_food(fruits)


#return values
def returnvalues(x):
    return 5 * x
print(returnvalues(8))
print(returnvalues(5))



