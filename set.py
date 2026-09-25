s={1,2,2,2,3}
print(len(s))  # Output: 3
print(s)  # Output: {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}
s.remove(2)
print(s)  # Output: {1, 3, 4}
s.pop()
print(s)  # Output: {3, 4}
s.clear()
print(s)  # Output: set()

empty_set = {}
print(type(empty_set))  # Output: <class 'dict'>


a={1, 2, 3}
a.union({1, 2, 3}, {3, 4, 5})  # Output: {1, 2, 3, 4, 5}
a.intersection({1, 2, 3}, {3, 4, 5})  # Output: {3}

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.intersection(s2))  # Output: {3}
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5}