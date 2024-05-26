x = list(input("enter a binary number "))
x.reverse()
value = 0
for i in range(len(x)):
    if x[i] == '1':
        value = value + pow (2 , i)
print (" the equivalent decimal number" , value)
