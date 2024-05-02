#write a python function to validate the Regular Expression.
import re
def validate_phone_number(phone):
    pattern = r'^[\w\s-]{3,20}$'  # Allow alphanumeric characters, spaces, and hyphens, with a length of 3 to 20 characters
    return bool(re.match(pattern, phone))
phone = "555-abc123"
if validate_phone_number(phone):
    print("Valid phone number")
else:
    print("Invalid phone number")
    import re
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
email_address = "1236gmail.com"
if validate_email(email_address):
    print("Email is valid.")
else:
    print("Email is invalid.")
