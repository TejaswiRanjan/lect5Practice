#print the multiplication table of a number n.

n = int(input("Enter a number : "))
print("Table of ",n," is : ")

for i in range(1,11):
    print(n, "x", i ,"=", n*i)