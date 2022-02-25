# import pandas as pd
# df = pd.read_excel('TestData.xlsx')
#
# print(df)
# print(pd.options.display.max_rows)

names=['john','sunny','jimmy','jolly','deep']
jnames=[name for name in names if name[0]=='j']
print(jnames)
digits = [2,44,22,21,33]
str_list = []
for i in digits:
    str_list.append(str(i))
filter = [int(number) for number in str_list if number[0]=="2"]
print(filter)