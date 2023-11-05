# # LIST ARE GOOD FOR  STORIGN A COLLECTION OF NAMES OR SCORES THAT CAN CHANGE IN THE LIFE OF A PROGRAM
#
# names_friends = ['milton', 'kinuthia', 'carl', 'john', 'puny', 'the donkey']
# for name in names_friends:
#     print(name)
#
# message = f"HI guys including you {names_friends[1].title()}"
# print(message)
names_friends = ['milton', 'kinuthia', 'carl', 'john', 'puny', 'the donkey']
del names_friends[0]
print(names_friends)
# # use the delete key if you dont want to use it at all again
#
# USE POP TP REMOVE THE LAST ELEMENT FROM A LIST AND CAN BE USED OTHERWISE
names_friends = ['milton', 'kinuthia', 'carl', 'john', 'puny', 'the donkey','freddy']
last_name_popped = names_friends.pop()
print(names_friends)
print(last_name_popped)
#
last_friend = names_friends.pop()
message = f"The last friend i had was {last_friend}."
print(message)
first_friend = names_friends.pop(1)
message = f"The first friend i have ever had is {first_friend}."
print(message)
#
# the output is 3 names as the rest have been poped, removed
print(names_friends)

It_courses = ['business information technology','computer science','information technology','computer technology']
It_courses.remove('business information technology')
print(It_courses)

best_choice = 'computer science'
It_courses.remove(best_choice)
print(It_courses)
print(f"\n\tThe course known as  {best_choice} is the most all rounded.")



guest_list = ['kinuthia','bahanye','lambistic','chira','brian']
invite1 = f"Hi {guest_list[0]} your invited over to dinner"
invite2 = f"\nHi {guest_list[1]} your invited over to dinner"
invite3 = f"\nHi {guest_list[2]} your invited over to dinner"
invite4 = f"\nHi {guest_list[3]} your invited over to dinner"
invite5 = f"\nHi {guest_list[4]} your inivted over to dinner"

print(invite1,invite2,invite3,invite4,invite5)

guest_gone_is = guest_list.pop(0)
message = f"The guest who cant make it is {guest_gone_is}."
print(message)

print(guest_list)

guest_list.insert(0,"wambo")

print(guest_list)

invite1 = f"Hi {guest_list[0]} your invited over to dinner"
invite2 = f"\nHi {guest_list[1]} your invited over to dinner"
invite3 = f"\nHi {guest_list[2]} your inited over to dinner"
invite4 = f"\nHi {guest_list[3]} your inited over to dinner"
invite5 = f"\nHi {guest_list[4]} your inited over to dinner"

print(invite1,invite2,invite3,invite4,invite5)

invite_1 = f"Hi {guest_list[0]} i found a bigger dining table"
invite_2 = f"\nHi {guest_list[1]} i found a bigger dining table"
invite_3 = f"\nHi {guest_list[2]} i found a bigger dining table"
invite_4 = f"\nHi {guest_list[3]} i found a bigger dining table"
invite_5 = f"\nHi {guest_list[4]} i found a bigger dining table"
print(invite_1,invite_2,invite_3,invite_4,invite_5)
guest_list.insert(0,"ale")
guest_list.insert(3,"victor")
guest_list.append("kifee")
print(guest_list)

this_list = guest_list[0:7]
message = f"Excuse guys {this_list} i can only invite 2 people for dinner am sorry please do pardon me."
print(message)

removed = guest_list.pop()
message = f"Am really sorry {removed.title()} you cant be invited."
print(message)

removed1 = guest_list.pop(1)
message1 = f"Am really sorry {removed1.title()} you cant be invited over for dinner."
print(message1)

remainder = guest_list[4]
invited_remainder = f"Hi {remainder} your invited over."
print(invited_remainder)

del guest_list[0:7]
print(guest_list)

world_tour = ['USA','ENGLAND','SWITZERLAND','CAPE TOWN','AUSRALIA','VIETNAM','ROMANIA','BULGARIA']
for tour in world_tour:
    print(tour)
print(world_tour)

print(sorted(world_tour))

print(world_tour)

world_tour.sort(reverse=True)
print(world_tour)

print("----------------------------------------------------------------------------------")

world_tour.reverse()
print(world_tour)

# print("----------------------------------------------------------------------------------")

print(sorted(world_tour))

# print("----------------------------------------------------------------------------------")

world_tour.sort(reverse=True)
print(world_tour)

print("----------------------------------------------------------------------------------")


print(len(guest_list))

# SLICING THROUGH A LIST

CodingSchools = ['Moringa','Emobilis','Institute of Software Technologies']
print("Here are the list of the best coding schools in Nairobi:")
for CodingSchool in CodingSchools[:3]:
    print(CodingSchool)

# IMPORTANCE EG GAME CAN BE USED IN A GAME TO GET THE TOP THREE SCORES OF A PLAYER BY SORTING THEM IN REVERSE ORDER


# COPYING A LIST ONTO A NEW LIST
Unis = ["Kabarak","Cuea","Machakos","Ku","Jkuat"]

RealUnis = Unis[:]

print(f"This are the universities :\n{Unis}")
#
RealUnis.append("Strathmore")
Unis.append('Riara')
print(f"This are the real univeristies in kenya:{RealUnis}")
print(f"This are the average univeristies in kenya: {Unis}")
#
# # Uniss = ["Kabarak","Cuea","Machakos","Ku","Jkuat"]
# # RealUniss = Uniss
# # print(f"This are the universities :\n{Uniss}")
# # RealUniss.append("Strathmore")
# # print(Uniss)
#
# pizzas = ["bbq","pepperoni","hawaian","meat deluxe","bbq chicken"]
# friends_pizza = pizzas[:4]
#
# pizzas.append('lambistizza')
# friends_pizza.append('kinalizia')
#
# print(f"My fav pizzas are :\n {pizzas}")
# print(f"My friends fav pizzas are :\n {friends_pizza}")
#
#
# list1 = [['cat','dog',],['elephant','parrot']]
# list2 = list1.copy()
# list1[0][0] = ('elephant')
# print(list1[0],list2[0])
#
#
#
