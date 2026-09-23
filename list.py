marks =[99, 98, 97, 96,"abc", 95]
print(marks[0])  # Output: 99
print(len(marks))  # Output: 5
print(marks[-1])  # Output: 95
print(marks[1:4])  # Output: [98, 97, 96]
print(type(marks))  # Output: <class 'list'>

age = [20, 21, 22, 23, 24]
age.append(25)
print(age)  # Output: [20, 21, 22, 23, 24, 25]
age.insert(2, 21.5)
print(age)  # Output: [20, 21, 21.5, 22, 23, 24, 25]
age.remove(20)
print(age)  # Output: [21, 21.5, 22, 23, 24, 25]
age.reverse()
print(age)  # Output: [25, 24, 23, 22, 21.5, 21]



#lists using for loop
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)  # Output: 1 2 3 4 5
    
    
#search any element in list
l= [1,2,3,4,5]
x =4
idx=0 
for val in l:
    if(val == x):
        print(f"{x} found at index = {idx}")
        break
    idx += 1