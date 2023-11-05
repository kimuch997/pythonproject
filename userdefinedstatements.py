def bmi (weight,height):
    bmi = weight/(height*height)
    if bmi <= 18:
        print("underweight")
    elif bmi > 18.1 and bmi <=29 :
         print("normal weight")
    elif bmi >29.1 and bmi < 34:
        print("overweight")
    else:
     print("obese")

weight = float(input("enter weight:\n"))
height = float(input("enter height:\n"))
bmi(weight,height)

def login(name,email,password):
    if name == "jane" and email =="jane@example" and password == "jane123":

        weight = float(input("enter weight\n"))
        height = float(input("enter height\n"))
        bmi(weight,height)
    else:
        print("login failed")

name = input("enter name :\n")
email = input("enter email:\n")
password = input("enter password:\n")

login(name,email,password)





