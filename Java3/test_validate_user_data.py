import pytest
from validate_user_data import validate_user_data

def test_valid_data():
    input_data = {
        "username": "valid_user123",
        "email": "test@example.com",
        "password": "Passw0rd!",
        "age": 25,
        "referral_code": "ABCDEFGH"
    }
    result = validate_user_data(input_data)
    assert result["is_valid"] is True
    assert result["errors"] == {}

def test_missing_userdata():
    result = validate_user_data(None)
    assert result["is_valid"] is False
    assert "global" in result["errors"]

@pytest.mark.parametrize("username, expected_error", [
    (None, "Username is required"),
    ("", "Username is required"),
    ("ab", "Username must be between 3 and 20 characters"),
    ("a"*21, "Username must be between 3 and 20 characters"),
    ("user!", "Username can only contain letters, numbers, and underscores"),
])
def test_username_validation(username, expected_error):
    input_data = {
        "username": username,
        "email": "a@b.com",
        "password": "P4ssword!"
    }
    result = validate_user_data(input_data)
    assert result["is_valid"] is False
    assert result["errors"]["username"] == expected_error

@pytest.mark.parametrize("email, expected_error", [
    (None, "Email is required"),
    ("", "Email is required"),
    ("invalid-email", "Invalid email format"),
])
def test_email_validation(email, expected_error):
    input_data = {
        "username": "user123",
        "email": email,
        "password": "P4ssword!"
    }
    result = validate_user_data(input_data)
    assert result["is_valid"] is False
    assert result["errors"]["email"] == expected_error

@pytest.mark.parametrize("password, expected_error", [
    (None, "Password is required"),
    ("", "Password is required"),
    ("short", "Password must be at least 8 characters long"),
    ("Password", "Password must contain at least one number"),
    ("Passw0rd", "Password must contain at least one special character"),
])
def test_password_validation(password, expected_error):
    input_data = {
        "username": "user123",
        "email": "a@b.com",
        "password": password
    }
    result = validate_user_data(input_data)
    assert result["is_valid"] is False
    assert result["errors"]["password"] == expected_error

@pytest.mark.parametrize("age, expected_error", [
    ("old", "Age must be a number"),
    (17, "User must be at least 18 years old"),
])
def test_age_validation(age, expected_error):
    input_data = {
        "username": "user123",
        "email": "a@b.com",
        "password": "P4ssword!",
        "age": age
    }
    result = validate_user_data(input_data)
    assert result["is_valid"] is False
    assert result["errors"]["age"] == expected_error

@pytest.mark.parametrize("referral_code, expected_error", [
    (12345678, "Referral code must be a string"),
    ("ABC", "Referral code must be exactly 8 characters"),
])
def test_referral_code_validation(referral_code, expected_error):
    input_data = {
        "username": "user123",
        "email": "a@b.com",
        "password": "P4ssword!",
        "referral_code": referral_code
    }
    result = validate_user_data(input_data)
    assert result["is_valid"] is False
    assert result["errors"]["referral_code"] == expected_error
