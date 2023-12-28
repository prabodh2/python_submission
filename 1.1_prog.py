def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest
# Input values from the user
principal_amount = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest per year: "))
time_period = float(input("Enter the time (in years): "))
# Calculate simple interest using the function
simple_interest = calculate_simple_interest(principal_amount, rate_of_interest, time_period)
# Display the result
print(f"Simple Interest: {simple_interest}")
