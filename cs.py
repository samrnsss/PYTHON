age = 21
if age >=18:
    print("You are an adult.")
    print("You can vote.")
else:
    print("You are a minor.")
    
    
    

color = input("enter color:")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Caution")
elif color == "green":
    print("Go")
else:
    print("Invalid color")
    
    

username = input("enter username:")
password = input("enter password:")
if username == "admin" and password == "password123":
    print("Login successful")
elif(username != "admin" ):
    print("Login successful")
else:
    print("Login failed")
    
    
# multuple of 5
n=int(input ("enter number:"))
if (n%5 == 0):
    print("multiple of 5")
else:
    print("not multiple of 5")
    