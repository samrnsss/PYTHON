#function definition
def sum(a,b):   #a and b are parameters
    s = a+b
    return s
#function call
ans = sum(2,3)  #2 and 3 are arguments
print("The sum is:", ans)



#lambda function
avg = lambda m,n: (m+n)/2
print(avg(2,3))