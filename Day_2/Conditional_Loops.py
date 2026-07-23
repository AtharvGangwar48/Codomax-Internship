print("Checking numbers between 1 and 10:")

# Loop iterates through a sequence of numbers from 1 up to (but excluding) 11
for number in range(1, 11):
    # Using the modulus operator (%) to check for a remainder
    if number % 2 == 0:
        print(f"Number {number} is EVEN")
    else:
        print(f"Number {number} is ODD")
