# UNCHANGABLE LIST
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

my_t = (3,)
print(my_t[0])

# Although you can’t modify a tuple, you can assign a new value to a variable
dimensions = (200,50)
print("original dimensions")
for dimension in dimensions:
    print(dimension)

print("modified dimension")
dimensions = (207,5560)
for dimension in dimensions:
    print(dimension)

Transport = ("tomatoes","capsicums","potatoes","onions","malenges")
for transport in Transport:
    print(transport)

# Transport[0] = 'Nyanya'
#
# print(Transp$ort[0])