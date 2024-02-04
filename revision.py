fruits = ["cherry", "melon", "apple", "pawpaw"]
numbers =[ 1, 2, 3,4]

print(fruits[0])
fruits.insert(1, "orange")
print(fruits)


countries = ["Kenya", "Ghana", "Mali"]
countries.append("Angola")
print(countries)

colbyFrech = ["Cote Divore", "Guinea"]
countries.extend(colbyFrech)
print(countries)

#delete and clear list items
countries.remove("Mali")
countries.pop(1)
print(countries)

countries.clear()
print(countries)

#tuples

girls = ("Linda", "Nina", "Jackie")
number = (1, 2, 3)

print(girls)


#concanate tuples
integers1 = (1, 2, 3)
integers2 = (4, 5, 6)

allTuples = integers1 + integers2
print(allTuples)

print(len(girls))
print(type(girls))
print(type(colbyFrech))

#sets
professions = (("pilot", "Engineer", "Doctor"))
print(professions)
professions1={}
print(type(professions1))

professions2 = set()
print(type(professions2))

#no accessing for set items
months = {"June", "July", "October"}

for item in months:
    print(item) 

#to check whether value is true
    print("April" in months)
    print("June" in months)