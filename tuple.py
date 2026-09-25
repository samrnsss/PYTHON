tup = (1,2,3,4,5)
print(tup)  # Output: (1, 2, 3, 4, 5)
print(tup[0])  # Output: 1
print(type(tup))  # Output: <class 'tuple'>
print(len(tup))  # Output: 5


t=("1")
s=("abc")
print(t)  # Output: ('1',)
print(type(t))  # Output: <class 'tuple'>
print(s)  # Output: ('abc',)
print(type(s))  # Output: <class 'tuple'>


t1= (1,2,3,4,5)
for val in t1:
    print(val)  # Output: 1 2 3 4 5 (each on a new line)
 
 
    
t2 = (1, 2, 3, 4, 5)
sum = 0
for val in t2:
    sum += val
    print(f"the sum of the tuple is: {sum}")  # Output: the sum of the tuple is: 1, 3, 6, 10, 15 (each on a new line)


a= (1, 2, 2,4,6,3,1,2,3, 4, 5)
print(a.count(2))  # Output: 3
print(a.index(4))  # Output: 3
print(a.count(1))  # Output: 2