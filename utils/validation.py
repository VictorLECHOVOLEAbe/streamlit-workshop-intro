import streamlit as st
import re

def validate_name(name: str) -> bool:
    """
    Validates that the name contains only letters and spaces and is of appropriate length.
    Args:
        name (str): The name to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    if not name:
        st.warning("Please enter your name to continue.")
        return False
    if len(name) < 3:
        st.error("The name must have at least 3 characters.")
        return False
    if len(name) > 50:
        st.error("The name cannot exceed 50 characters.")
        return False
    if not name.replace(" ", "").isalpha():
        st.error("The name must contain only letters and spaces.")
        return False
    return True


def validate_email(email: str) -> bool:
    """
    Validates the email format.
    Args:
        email (str): The email address to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    if not email:
        st.warning("Please enter your email to continue.")
        return False
    if len(email) < 5:
        st.error("The email must have at least 5 characters.")
        return False
    if len(email) > 100:
        st.error("The email cannot exceed 100 characters.")
        return False
    if "@" not in email or "." not in email:
        st.error("Please enter a valid email address.")
        return False
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        st.error("Please enter a valid email address.")
        return False
    return True