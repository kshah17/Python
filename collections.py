# Collections
## grouping of data
### can be a list
'''
list_1 = [10, 0.1, "hello,wolrd", True]
names = ["Dave", "Steve", "Anne", "Liz"]
towns = ["London, Manchester, Liverpool"]
animals = ["Dog, Cat, Bird"]

all_things = [names, towns, animals]
##              0      1       2
print(names[0])
print(names[1])

## print(all_things[1][1])
##             List 1, London


animals.append("Horse")
animals.remove("Dog")
animals.remove(animals[2])

print(animals)

towns.reverse()
print(towns)

animals.count("Dog")
print(animals.count("Dog"))


new_string - "and".join(animals)
## joins everything in the list and uses "" as a sepatator 
print(new_string)

names.sort()
print(names)

## dictionarys - made up of tuples, immutable

my_new_tuple = ("Kev", 0, 4, False, 0.6)
print(my_new_tuple)
'''