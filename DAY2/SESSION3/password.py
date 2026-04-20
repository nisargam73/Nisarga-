def has_min_length(password, min_len=8):
    return len(password) >= min_len


def has_uppercase(password):
    for ch in password:
        if ch.isupper():
            return True
    return False


def has_lowercase(password):
    for ch in password:
        if ch.islower():
            return True
    return False


def has_digit(password):
    for ch in password:
        if ch.isdigit():
            return True
    return False


def has_special_char(password, specials="!@#$%^&*"):
    for ch in password:
        if ch in specials:
            return True
    return False


def analyze_password(password):
    score = 0
    failed_checks = []

    if has_min_length(password):
        score += 1
    else:
        failed_checks.append("Minimum Length")

    if has_uppercase(password):
        score += 1
    else:
        failed_checks.append("Uppercase")

    if has_lowercase(password):
        score += 1
    else:
        failed_checks.append("Lowercase")

    if has_digit(password):
        score += 1
    else:
        failed_checks.append("Digit")

    if has_special_char(password):
        score += 1
    else:
        failed_checks.append("Special character")

    # Strength labeling
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return (strength, score, failed_checks)


# ----------- User Input -----------
password = input("Enter password: ")
result = analyze_password(password)

print("Output:", result)