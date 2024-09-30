import re

email_condition = r'^[a-z]+[0-9][\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# Explanation:
# ^[a-z0-9]+ - ensures that the email starts with a combination of lowercase letters or digits
# [\._]? - optionally matches a dot (.) or underscore (_) after the initial part
# [a-z0-9]+ - allows lowercase letters or digits before the @ symbol
# [@] - requires an "@" symbol
# \w+ - ensures a domain name after the @ (alphanumeric and underscore)
# [.] - requires a dot for the domain extension
# \w{2,3}$ - requires a 2 or 3 letter domain extension, like .com, .in, etc.

def email_validate():
    user_input = input("Enter your email: ")
    if re.match(email_condition, user_input):
        print("Email is valid")
    else:
        print("Email is not valid")

email_validate()



   