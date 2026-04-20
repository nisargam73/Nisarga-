import streamlit as st

st.title("Password Checker")
st.write("Check your password strength below.")

# --- Validation Functions ---
def has_min_length(password, min_len=8):
    return len(password) >= min_len

def has_uppercase(password):
    return any(ch.isupper() for ch in password)

def has_lowercase(password):
    return any(ch.islower() for ch in password)
    
def has_digit(password):
    # .digit() isn't a method; .isdigit() is!
    return any(ch.isdigit() for ch in password)
       
def has_special_char(password, special="!@#$%^&*"):
    # There is no .special_char() method; we check if char is in our string
    return any(ch in special for ch in password)

def analysePassword(password):
    strength = 0
    failed = []

    if has_min_length(password):
        strength += 1
    else:
        failed.append("Minimum length (8 characters) not met")

    if has_uppercase(password):
        strength += 1
    else:
        failed.append("Missing uppercase letter")

    if has_lowercase(password):
        strength += 1
    else:
        failed.append("Missing lowercase letter")

    if has_digit(password):
        strength += 1
    else:
        failed.append("Missing a digit")  

    if has_special_char(password):
        strength += 1
    else:
        failed.append("Missing a special character (!@#$%^&*)")

    # Determine Rating
    if strength <= 2:
        flag = "Weak"
    elif strength <= 4:
        flag = "Moderate"
    else:
        flag = "Very Strong"

    return flag, strength, failed

# --- Streamlit UI ---
password = st.text_input("Enter the password", type="password")

if st.button("Analyse Password"):
    if not password:
        st.warning("Please enter a password first.")
    else:
        flag, strength, failed = analysePassword(password)
        
        st.subheader("Results")
        
        # Displaying metrics
        col1, col2 = st.columns(2)
        col1.metric("Strength Score", f"{strength}/5")
        col2.metric("Rating", flag)

        if failed:
            st.error("Improvement needed:")
            for issue in failed:
                st.write(f"- {issue}")
        else:
            st.success("Perfect! Your password meets all security criteria.")