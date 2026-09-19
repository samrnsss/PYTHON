for i in range(5):
    print(i)
for j in range(5, 10):
    print(j)
#to print odd nums
for k in range(1,16,2):
    print(k)
#to print even nums
for l in range(2, 21, 2):
    print(l)
    
    
    
#print sum of first n natural numbers
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("The sum of first", n, "natural numbers is:", sum)