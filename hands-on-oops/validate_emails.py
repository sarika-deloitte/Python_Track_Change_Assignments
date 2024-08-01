#  Q5. Write a regex expression to validate emails which allows only (these two special symbols (.  and -) before @ symbol.
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
emails = [
    "valid.email@example.com",
    "valid-email@example.com",
    "invalid_email@example.com",  # Invalid because of underscore before @
    "invalid.email@.com",         # Invalid because of dot immediately after @
    "invalid-email@example",      # Invalid because TLD is less than 2 characters
    "valid.email@sub-domain.example.com"
]

for email in emails:
    print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")
