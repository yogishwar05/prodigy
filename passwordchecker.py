import re

def assess_password_strength(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/~`]', password))

    score = 0
    feedback = []

    # Length check
    if length >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if has_upper:
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Lowercase check
    if has_lower:
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Digit check
    if has_digit:
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Special character check
    if has_special:
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Feedback
    if score == 5:
        feedback.append("Password strength: Strong")
    elif score >= 3:
        feedback.append("Password strength: Medium")
    else:
        feedback.append("Password strength: Weak")

    return feedback

def main():
    password = input("Enter your password: ")
    feedback = assess_password_strength(password)
    for msg in feedback:
        print(msg)

if __name__ == "__main__":
    main()
