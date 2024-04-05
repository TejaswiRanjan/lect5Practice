# Search for a number X in this tuple using loop :
# [1,4,9,16,25,36,49,64,81,100]
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the element that you want to search : "))
i = 0
while i < len(tup):
    if (tup[i] == x):
        print("Element found at index ", i)
        print("Done")
        break
    else:
        print("Finding...")
        i+=1
else:
    print("Element not found ")

print("End")
