thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1966,
  "year": 2020
}
print(thisdict)
print(len(thisdict))


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))

thisdictionary = dict(name = "John", age = 36, country = "Norway")

print(thisdictionary)
print("--------------------------------------------")

# ADDITION OF ITEMS ON A DICTIOANRY AND CHECKING THE TYPES OF THOSE ITEME

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"],
    "model":"kinuthia"
}
b =thisdict["year"]

print(b)

x= thisdict.keys()

print(x)

thisdict["engine"] = 8
thisdict["engine"] = "kinuthia 9 piston engine"
thisdict.update({"colour": "orange"})

print(x)


c = thisdict.values()

print(c)

q = thisdict.items()
print(q)
if "engine" in thisdict:
    print("Yes,'model' is in thisdict. ")

# REMOVAL OF ITEMS

Mylistdict = {
  "levels":"levl1",
  "intensity":"hard",
  "lambistry":"punidom"

}
