#create a function to request a list of students
#and print all the names longer than 4 characters but
#shorter than 7 characters


#Q2 of the received names in question 1 sort and print
# out all the names that are longer than 7 characters


#of the received names identify and print all the names
# that are


def print_students(students):
    for student in students:
        if len(student)> 4 and len(student) < 7:
            print(student)
students = ["alice", "anthonykim","kimathi","marvin","ahmed","mama"]
print_students(students)


def print_students(students):
    students= sorted(students)
    for student in students:
        if len(student)>7:
            print(student)
students = ["alice", "anthonykim","kimathii","marvin","ahmed","mama"]
print_students(students)
def print_palindromic(students):
    for student in students:
        if student == student[::-1]:
            print(student)
students = ["alice", "anthonykim","kimathi","marvin","ahmed","mama"]
print_palindromic(students)


print("-------------------------------")

# def list_of_students():
#     x = (int(input("How may students are you registering?\n")))
#     my_list = []
#
#     for i in range(x):
#         name = (input("enter name: "))
#         my_list.append(name)
#
#     print("Names with more than 4 characters but less than 7 characters are:")
#
#     for name in my_list:
#          if len(name)> 4 and len(name)<7:
#             print(name)
#     print("Names with more than 7 characters are:")
#
#     for name in my_list:
#         if len(name) > 7:
#             print(name)
#
#     print("palindromic names")
#     for name in my_list:
#         if name == name [::-1]:
#             print(name)
# list_of_students()


print("----------------------")

def challenge(names):
    print("names >4 characters but < 7 characters")
    for name in names:
        if len(name) >4 and len(name) < 7:
            print(name)
    print("names > 7 characters")
    names.sort()
    for name in names:
        if len(name) > 7:
            print(name)

    print("palindromic names")
    for name in names:
        if name == name [::-1]:
            print(name)

names = ["anthony","mark","brian","ashley","mutembei","kinuthia","bob"]
challenge(names)


