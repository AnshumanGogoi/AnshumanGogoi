

s1 = 'silentt'
#print(sorted(s1))
s2 = 'listen'
#print(sorted(s2))
def check(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")
check(s1,s2)


# if __name__ == '__main__':
#     word1, word2 = 'listen', 'silent'
#     check(word1, word2)