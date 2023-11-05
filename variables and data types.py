character_name = "john"
character_age = "35"

print("There was a man named " + character_name + ",")
print("He was 70 years old.")


character_name="mike"
print("He really liked the name " + character_name + ",")
print("But he didnt like being " + character_age + ",")


character_nick_name="Kinuthia"
phrase="House manor is realy cool innit.There was once a man named " + character_nick_name + "a" \
       " lambistoc man but" \
       " changed his ways once he found out" \
       " he was being puny this is after he found out that he was being played. "
print(phrase.upper())
print(len(phrase))
print(phrase[186])
print(phrase[7])
print(phrase.index("rea"))
print(phrase.replace("House","elephant"))


is_male = False
is_tall = True

if is_male or is_tall:
    print("you are a male")
else:
    print("you are not  male and not tall ")



fruits = ("apples","mangoes","pineapples","banana.")
print(fruits[::3])

print(help(fruits))

print("-------------------------------------------")
#FUNCTIONS
#arguments

def funcion(name):
    print(name,"kimathi")
funcion("anthony")
funcion("kimuch")
funcion("marcel")


def function(name1,name2):
    print(name1,"and",name2,"are good boys.")
function("alex","kim")


#arbitary args = if you dont know how many args will be passed inside your function
#single *
def function(*kids):
    print(kids[0],"is really behaved.")
function("anthony","esther","wangechi")


# keyword = args the order doesnt matter
def function(child1,child2,child3):
    print("my eldest children are",child2,child1,"and",child3)
function(child1 = "kim",child2 = "anthony",child3 = "mutethia")

#of you dont know how may keuw
def function(**kid):
    print("my oldest child is",kid["name"])
function(name = "namu",names = "kinuthia" , nammes = "lambistic")


#list as an argument
def function(fruits):
    for x in fruits:
        print(x)
fruits = ["apple","popo","pieapple"]
function(fruits)


print("------------------------------")
#DATA TYPES
#Lists
thislist = ["kim","jones","terry","anthony"]
print(thislist)

thislist = list["kim","jones","terry","brian"]
print(thislist)

#changing the item value
list = ["anthony","kim","mutethia"]
list[1] = "kinuthia"
print(list)

#range of item values
list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list[1:4] = ["pineapple","watermelon"]
print(list)

#inserting
lisst = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
lisst.insert(2,"watermelon")
print(lisst)

#append
lisst = ["kinuthia","lambistic","puny"]
list.append("mother")

#extend
foods = ["ham","pizza","chips","meetpie","lazania"]
drinks = ["gin","whiskey","soda","smoothie","milkshake"]

foods.extend(drinks)
print(foods)

#removing
songs = ["daylight","money trees","still","juicy"]
songs.pop(1)
print(songs)

songs = ["daylight","money trees","still","juicy","very friends"]
songs.remove("money trees")
print(songs)
#deleting list

# courses = ["computer technology","computer science","software engineering","information technology"]
# del courses
# print(courses)

courses = ["computer technology","computer science","software engineering","information technology"]
courses.clear()
print("courses")


#loops
roads = ["mbagathi road","moi ave","kenyatta av","wangari maathai road"]
for road in roads:
    print(road)

print("---------------------")

courses = ["computer technology","computer science","software engineering","information technology","business information technology"]
for i in range(len(courses)):
    print(courses[i])

print("---------------")


# #NOT UNDERSTOOD
# foods = ["ham","pizza","chips","meetpie","lazania"]
# food = 0
# while food < len(foods):
#      print(foods[food])
#      food = food + 1
#
# #List comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = []
#
# for fruit in fruits:
#     if "a" in fruit:
#         new_list.append(fruit)
# print(new_list)
#
# print("----------------")
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [fruit for fruit in fruits  if "a" in fruit]
#
#
# print(newlist)
#
#
# #SORT LIST
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
#
#
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse=True)
# for list in thislist:
#     print(list)
# print(thislist)
#
#
# kinuthias = ["kibe","andrew","nganuthia","wajesus"]
# kinuthias.reverse()
# for kinuthia in kinuthias:
#     print(kinuthia)
# print(kinuthias)
#
# print("-------------------------------------------------")
#
# # CUSTOMIZE SORT FUNCTION
# # CUSTOMIZE SORT FUNCTION CUSTOMIZE SORT FUNCTION
# # CUSTOMIZE SORT FUNCTION
#
#
# # case sensitive
# thislist = ["oRange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(key = str.lower)
#
# print("---------------------------------------------")
# # copying list
#
# kinuthias2 = ["kibe","andrew","nganuthia","wajesus"]
# names = kinuthias2.copy()
# for name in names:
#     print(name)
# print(names)
#
# print("------------------------------------")
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
#
# for content in list2:
#   list1.append(content)
#
# print(list1)
#
# #OR
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
#
# list1.extend(list2)
# print(list1)
#
#
#
# x = range(6)
# print(x)
message = "kinuthia is lambistic as fuck"
print(message)
message = "doing that now"
print(message)