# Python practice
info = {
    "name": "aashna",
    "cgpa":9.0,
    "age": 20,
    "subject": ["maths", "science", "english"],
    3.14:"PI"
}
print(type(info))  # Output: <class 'dict'>
print(info)  # Output: {'name': 'aashna', 'cgpa': 9.0, 'age': 20, 'subject': ['maths', 'science', 'english']}
print(info["name"])  # Output: aashna
print(info["cgpa"])  # Output: 9.0
print(info[3.14])

dict_keys = list(info.keys())
print(dict_keys)  # Output: dict_keys(['name', 'cgpa', 'age', 'subject', 3.14])
print(type(dict_keys))  # Output: <class 'list'>
print(info.values())  # Output: dict_values(['aashna', 9.0, 20, ['maths', 'science', 'english'], 'PI'])
print(info.values())  # Output: ['aashna', 9.0, 20, ['maths', 'science', 'english'], 'PI']
print(info.items())  # Output: dict_items([('name', 'aashna'), ('cgpa', 9.0), ('age', 20), ('subject', ['maths', 'science', 'english']), (3.14, 'PI')])
print(info.get("name"))  # Output: aashna
print(info.update({"name": "Aashna", "age": 21}))  # Updates the name and age
print(info)  # Output: {'name': 'Aashna', 'cgpa': 9.0, 'age': 21, 'subject': ['maths', 'science', 'english'], 3.14: 'PI'}
