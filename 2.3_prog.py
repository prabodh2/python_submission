def extract_username_and_domain(email):

    # Split the email address into username and domain parts
    username, domain = email.split('@', 1)
    return username, domain

# Input an email address from the user
email_address = input("Enter an email address: ")

# Call the function to extract username and domain
username, domain = extract_username_and_domain(email_address)

# Display the result
print("Username:", username)
print("Domain:", domain)
