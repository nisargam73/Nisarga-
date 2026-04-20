def has_min_length(password, min_len=8):
    return len(password) >= min_len


def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


def has_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def has_special_char(password, specials="!@#$%^&*"):
    for char in password:
        if char in specials:
            return True
    return False


def analyze_password(password):
    checks = {
        "Minimum length": has_min_length(password),
        "Uppercase": has_uppercase(password),
        "Lowercase": has_lowercase(password),
        "Digit": has_digit(password),
        "Special character": has_special_char(password),
    }

    score = sum(checks.values())
    failed_checks = [name for name, passed in checks.items() if not passed]

    if score <= 2:
        strength_label = "Weak"
    elif score == 3:
        strength_label = "Medium"
    elif score == 4:
        strength_label = "Strong"
    else:
        strength_label = "Very Strong"

    return strength_label, score, failed_checks


password1 = "Abc@1234"
password2 = "abcdefgh"

print(password1, "->", analyze_password(password1))
print(password2, "->", analyze_password(password2))
