""""Demonstrate the behavior of conditionals"""

user_input: str = input("Pick a number: ")
print(type(user_input))
user_number: int = int(user_input)
print(type(user_number))

# if a number is >10, print "small"
if user_number <10 :
    print("small")
else: # user_number >= 10
    print("big")

if user_number % 2 == 0 :
    print("even")
else: # user_number is odd
    print("odd")

print(int(“20”))

print(int(8.0) + 10 / int("0"))
print(int("0"))