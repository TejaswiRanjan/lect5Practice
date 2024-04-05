#WAP to find the sum of first n numbers.(using while)
sum = 0
n = int(input("Enter a number : "))
i=1
while i<=n:
    sum = sum + i
    i+=1

print("Sum of first n natural number is : ",sum)