print("June-9th-2025: Learning Typecasting")

# Typecasting = The process of converting a value of one data type to another
#               (string, integer, float, boolran)
#               Explicit vs Implicit



# Explicit Typecasting
# it's when data is converted to a defferent format manually
name = "Lamar"
age = 21
years = 21
gpa = 1.9
student = True

# type()
type(name) # type is use to check what type of variable is shown.

print(type(name))
print(type(age))
print(type(gpa))
print(type(student)) 

# now lets explicit typecast the variables above
age = float(age)
print(age)

# or:
print(float(years))

# typecasting integers to booleans
# it will all turn out True if the interger is anything but 0

print(bool(age))

years = bool(years)
print(years)

# You can also use typecasting to check for user input, in example:


dark_web_name = input("Enter your dark web name.'not your actual': ")

print(bool(dark_web_name))


# Implicit Typecasting
# It's when data is coverted to another format automatically
x = 2
y = 2.0

print(x/y) # The output is aoutomatically a float in the output: 1.0

# That is implicit Typecasting.



