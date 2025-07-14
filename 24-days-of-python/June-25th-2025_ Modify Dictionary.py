profile = {
    "name": "Lamar",
    "age": 23,
    "is_AI_Student": True
}
print(profile["name"])

profile["Location"] = "Kenya" # Add new key
profile["age"] = 24           # update 
del profile["is_AI_Student"]  # delete

print(profile)
