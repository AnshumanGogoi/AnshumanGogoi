"""country my love i"""
sentance = "i love my country"
words = sentance.split(" ")
####################
# print(words)
# words=words[-1::-1]
# print(words)
# outputstr=" ".join(words)
# print(outputstr)

"""i evol ym yrtnuoc"""
rev_str =[]

for i in words:
    rev_str.append(i[::-1])
    op_str = " "
    op_str = op_str.join(rev_str)
print(op_str)

import re
org_string = "Sample 11 String 42 -In 2020"
pattern = r'[0-9]'
# Match all digits in the string and replace them by empty string
mod_string = re.sub(pattern, '', org_string)
print(mod_string)
