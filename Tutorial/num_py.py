
import numpy as np
# a = np.zeros((5,5))
# print(a)
a= np.array([1,2,3])
b= np.array([4,5,6])
print(np.sum((a,b), axis=0))

s = "i love india"
words = s.split()
for word in words:
    print(word.capitalize(), end=" ")
# OP: I Love India 