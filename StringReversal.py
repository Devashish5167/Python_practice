# String Reversal

s= input("Enter a string: ")
print(s[::-1])

#Or 
s=input("Enter a string: ")
i=len(s)-1
result = " "
while i >= 0:
    result = result+s[i]
    i = i-1
print(result)