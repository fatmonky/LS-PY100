principal = 1000
annual_multiplier = 1.05
periods = 5
balance = (principal * (annual_multiplier**periods))
print(f"After {periods} years, you will have ${balance} in your account!")
annual_multiplier **= periods
balance = principal * annual_multiplier
print(f"using augmented assignment, after {periods} years, you will have ${balance} in your account!")
