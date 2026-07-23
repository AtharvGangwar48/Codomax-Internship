# Defining a reusable function with parameters and a return value
def convert_usd_to_eur(usd_amount, exchange_rate=0.92):
    """Calculates EUR value from USD using a specified rate."""
    converted_amount = usd_amount * exchange_rate
    return converted_amount

# Prompting user input
dollars = float(input("Enter amount in USD ($): "))

# Executing the function and capturing the returned data
euros = convert_usd_to_eur(dollars)

print(f"${dollars} USD is roughly equivalent to €{euros:.2f} EUR.")
