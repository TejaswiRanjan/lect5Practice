#WAP to find the factorial of first n number .(using for)

n = int(input("Enter  a number : "))
fact = 1

i = 1

while i<=n:
    fact = fact * i
    i+=1

print("The Factorail of ",n," is : ",fact)