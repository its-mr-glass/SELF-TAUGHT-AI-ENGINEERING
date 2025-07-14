name = ["Lamar", "Jones", "Ndubi"]

print(name[0])
print(name[1])
print(name[-1])

name.append("ID700605169")
name.remove("Jones")
name[1] = "Engineer"

print(name)

for name in name:
    print("AI Legend:", name)