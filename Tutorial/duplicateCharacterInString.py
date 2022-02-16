string = 'Python Programming'
dictionary = {}
for char in string:
    if( char in dictionary.keys()):
        dictionary[char] += 1
    else:
        dictionary[char]=1
for char in dictionary:
    print(char,' -> ',dictionary[char])

############## Duplicate character

string = 'Python Programming'
dictionary = {}
for char in string:
    if (char in dictionary.keys()):
        dictionary[char] += 1
    else:
        dictionary[char] = 1

duplicates = []
for char in dictionary:
    if (dictionary[char] > 1):
        duplicates.append(char)
print(duplicates)

################ Unique character


string = 'Python Programming'
dictionary = {}
for char in string:
    if (char in dictionary.keys()):
        dictionary[char] += 1
    else:
        dictionary[char] = 1

distinct_char = []
for char in dictionary:
    if (dictionary[char] == 1):
        distinct_char.append(char)

print(distinct_char)