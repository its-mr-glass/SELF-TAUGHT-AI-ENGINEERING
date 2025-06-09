# Typecasting = The process of converting a value of one data type to another
#               (string, integer, float, boolran)
#               Explicit vs Implicit



# Explicit
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

# now lest explicit typecast the variables above
age = float(age)
print(age)

# or:
print(float(years))