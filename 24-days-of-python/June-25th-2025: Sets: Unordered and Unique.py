# Sets - Unordered and Unique

unique_numbers = {1, 2, 3, 3, 2, 1}
print(unique_numbers)

# its great for:
#              removing duplicates
#              checking existence fast

if 2 in unique_numbers:
    print("Yes, 2 is here.")

# Use cases In AI:
#                 you get a dataset of labels: ["cat", "dog", "cat", "hourse"]    
# Using set() gives you all unique classes.