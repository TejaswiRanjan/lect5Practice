#print the multiplication table of a number n.

num = int(input("Enter a number : "))
i=1
while i<=10:
    print(num, "x", i, "=", num*i)
    i+=1