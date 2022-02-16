a = [1,2,5,7,3]
max = a[0]
for i in range(len(a)):
    if max < a[i]:
        max = a[i]
print(max)
secondMax = a[0]
for i in range(len(a)):
    if secondMax < a[i]:
        if a[i] != max:
            secondMax = a[i]
print(secondMax)