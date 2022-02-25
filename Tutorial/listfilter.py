numList = [10,2,6,88,99]
for i in range(len(numList)):
    for j in range(i+1, len(numList)):
        if (numList[i] > numList[j]):
            temp = numList[i]
            numList[i] = numList[j]
            numList[j] = temp

print("Element After Sorting List in Ascending Order is : ", numList)
numList.sort(reverse=True)
print(numList)


names=['john','sunny','jimmy','jolly','deep']
jnames = [name for name in names if name[0]=='j']
print(jnames)

digits = [2,44,22,21,33]
str_list=[]
for digit in digits:
    str_list.append(str(digit))
print(str_list)
filter = [int(number) for number in str_list if number[0]=="2"]
print(filter)


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()

print(Employee.empCount)


