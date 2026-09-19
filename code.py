print("Hello, World!")
print("This is a sample \n Python code.")

name= "shradha"
age=35
pi= 3.14
grade= None
num =2
isPrime= True
print("my name is", name)
print("my age is", age)
print("the value of pi is", pi)
print(type(age))
print(type(pi))
print(type(isPrime))
print(type(grade))
print("the value of num is", num)

full_name = "shradha sharma"
print(full_name[0])
print(full_name[1])
print(full_name[2])
print(full_name[3])
print(full_name[4])

a= 10
b= 5
# Arithmetic operations
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
# Relational operations
print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
# Assignment operations
x=10
x+=3
x-=2
x*=2
x/=4
x%=3

print(x)


# type conversion
ans = 5 + 10.0
print(type(ans))  
#  converts automatically to float (implicit type conversion)
print(ans) 
print(ans, type(ans))


#  converts to int (explicit type conversion) done by the programmer 
num1 = int(2+ 3.5)
print(num1)
print(type(num1))
print(num1, type(num1))


# the bool() function is used to convert a value to a Boolean value (True or False).
# it gives True for non-zero values and False for zero values.
val=bool(0)
print(val)
print(type(val))
num2= bool(10)
print(num2)
print(type(num2))


# input function
n=input("Enter your name: ")
print("Hello", n)

# sum of two nums
a1=input("Enter first number: ")
a2=input("Enter second number: ")
add = a1+a2
print("The sum of two numbers is:", add)
# this will concatenate the two strings instead of adding
# them as numbers. To fix this, we need to convert the i
# nputs to integers or floats before adding them. like this:
a1=int(input("Enter first number: "))
a2=int(input("Enter second number: "))
add = a1+a2
print("The sum of two numbers is:", add)



# calculate average
n1=int(input ("Enter first number: "))
n2=int(input ("Enter second number: "))
n3=int(input("enter the third number:"))
avg=float((n1+n2+n3)/3)
print("The average of three numbers is:", avg)

# write a progam that asks the user for their name and age, then prints a sentence like: "Hello, [name]! You are [age] years old."
namee=input('enter your name: ')
agee=int(input('enter your age: '))
print("Hello", namee, ", you're", agee, "years old!")