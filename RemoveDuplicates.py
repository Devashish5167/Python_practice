# Remove Duplicates in List

l1=eval(input("Enter a list of numbers: "))
print(l1)
l2 =[]
for each_value in l1:
    if each_value not in l2:
        l2.append(each_value)
print(l2)

#or
l1=eval(input("Enter a list of numbers: "))
s1 = set(l1)
print(s1)