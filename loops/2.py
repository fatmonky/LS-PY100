age = input("How old are you? ")
print(f"You are {age} years old.")

for difference in range(10, 50, 10):
    print(f"In {difference} years, you will be {int(age) + difference} years old.")
