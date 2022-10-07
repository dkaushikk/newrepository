a = "life"                          # traverse through a 'string'
for character in a:
    print(character, end=" ")
print()
for index in range(len(a)):
    print(index, a[index])

b = ["happy", "good", "relaxed", 1.58]   # traverse through a 'list'
for element in b:
    print(element)
for index in range(len(b)):
    print(index, b[index])

c = {"he", "she", 2.5, (1,2)}           # traverse through a 'set'
for element in c:
    print(element)
                                        # in 'set' indexing or slicing is not possible so 'range()' is not used


d = {1: 'a', 2: 'b'}       # traverses through a dictionary
for key in d:
    print(key)             # returns 'keys' in a dictionary
for keys_value in d:
    print(d[keys_value])   # returns 'values' of the 'keys'