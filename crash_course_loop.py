magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"{magician.title()},i can't wait to see your next trick\n")
# WATCH OUT FOR INDENTATION ERRORS WHICH CAN LEAD THE CORRECT OUTPUT TO BE PRINTED
# INDENT IT IN THE LOOP IF NEEDED TO BE REPEATED

print(f"Thank you guys that was a great magic show")

universities = ['CUEA', 'MACHAKOS UNIVERSITY', 'KU', 'JKUAT', 'MMU']
for university in universities:
    print(university)

    print(f"{university} is really great.\n")

prefered_university = universities.pop(2)
deserved_uni = universities.pop(1)
going_uni = universities.pop(0)
print(f"I would prefer this university:{prefered_university},\n{deserved_uni}")
print(f"I would prefer this university:{deserved_uni}")
print(f"I would prefer this university:{going_uni}")

animals = ['DOG','CAT','CHICKENS']
for animal in animals:
 print(animal)
animal_0 = animals.pop(0)
animal_1 = animals.pop(1)

print(f"I really dont know about {animal}")
print(f"{animal_1} are really good if u only manage to teach them not to pee in the house. ")
print(f"I really dont know about {animal_0}")





