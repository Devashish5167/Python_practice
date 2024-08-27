# s = '-'.join(['a', 'b', 'c'])
# print(s)

# s = input("ENter a string: ")
# print(''.join(reversed(s)))

# s= input("Enter a string")
# temp = s.split()
# print(temp)

#or
# s="All the power is within you"
# print(s.split())

s= "ALl the power is within you"
temp = s.split()
print(temp)
result = []
i = len(temp)-1
while i>=0:
    result.append(temp[i])
    i = i-1
print(result)
output = ' '.join(result)
print(output)