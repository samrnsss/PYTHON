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