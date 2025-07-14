# Ask for a user's name, age and AI interest.
# Based on input, print a fun customized message like: "Hello Lamar! At 23, your AI Journey is just beginning. 
#                                                       Let's dominate this industry!"
# use: input(), if/else, functions.

print("Hello there user :)")

name = str(input("Please share your name with me here: "))
age = int(input("Your current age here: "))
ai_interest = str(input("And finally your interests in AI: "))

if age < 18:
    print(f"wow {name}, way to start at early age.")
else:
    print(f"Not to late for anything at {age} isn't that right {name} :)")

def greet(name):
    return f"It was an honour chatting and knowing you {name},at that age of {age} you can still do alot in AI."
print(greet(name))
