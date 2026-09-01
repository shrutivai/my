name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nStudent Information")
print("Name:", name)
print("Age:", age)
print ("Welcome to the online checking device")
if age >= 18:
    print("Status: Adult")
else:
    print("Status: Minor")