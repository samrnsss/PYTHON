# string = "hello world"
# #in => membership operator
# for var in string:
#     print(var)

# if 'z' in string:
#     print("o is present in the string")


# for i in range(5):
#     print(i)
#     print(i+1)
    
    
    
# word = "artificial intelligence"
# #count the numbers of i's => 5
# count = 0

# for ch in word:
#     if ch == 'i':
#         count += 1

# print("The number of i's in the word is:", count)

word = "artificial intelligence"
count = 0

for ch in word:
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count += 1

print("The number of vowels in the word is:", count)