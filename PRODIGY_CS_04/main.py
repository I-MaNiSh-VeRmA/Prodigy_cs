import re

def assess_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."
    
    # Check for uppercase letter
    if not re.search("[A-Z]", password):
        return "Password should contain at least one uppercase letter."
    
    # Check for lowercase letter
    if not re.search("[a-z]", password):
        return "Password should contain at least one lowercase letter."
    
    # Check for number
    if not re.search("[0-9]", password):
        return "Password should contain at least one number."
    
    # Check for special character
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password should contain at least one special character."
    
    return "Password is strong!"

def main():
    password = input("Enter your password: ")
    strength = assess_password_strength(password)
    print(strength)

if __name__ == "__main__":
    main()
