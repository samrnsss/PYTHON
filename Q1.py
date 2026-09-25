#give a list of tuples wirh info(name,subject):
#-> list all unique courses
#-> list student enrolled in each course
#-> create a dictionary (student , set of courses)

info = [
    ("alice", "aashna"),
    ("john", "maths"),
    ("jane", "science"),
    ("doe", "english"),
    ("alice", "science"),
    ("charlie", "maths"),
    ("john", "english"),
    ("jane", "maths"),
    ("doe", "science"),
    ("charlie", "english"),
]


# courses_set = set()
# for tup in info:
#     courses_set.add(tup[1])

# print(courses_set)  # Output: {'maths', 'science', 'english'}

# for name,course in info:
#     if(course == "english"):
#         print(name)  # Output: doe, john, charlie
        
        
dict = {}
for name , course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
    dict[name].add(course)
else:
    dict[name].add(course)

print(dict)  # Output: {'alice': {'aashna', 'science'}, 'john': {'maths', 'english'}, 'jane': {'science', 'maths'}, 'doe': {'english', 'science'}, 'charlie': {'maths', 'english'}}