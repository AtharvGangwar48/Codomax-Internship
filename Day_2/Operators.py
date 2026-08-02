# Accepting user inputs (Note: input() always captures data as a string)
length_input = input("Enter rectangle length: ")
width_input = input("Enter rectangle width: ")

# Casting strings into float numeric types so we can do math
length = float(length_input)
width = float(width_input)

# Using arithmetic operators (* for multiplication, + for addition)
area = length * width
perimeter = 2 * (length + width)

# Displaying calculated results
print("\n--- Calculations ---")
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
