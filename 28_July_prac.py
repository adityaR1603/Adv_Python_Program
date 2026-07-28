from datetime import datetime

# -------------------------------
# 1. Login Authentication Decorator
# -------------------------------
def login_required(func):
    def wrapper(is_logged_in):
        if is_logged_in:
            return func(is_logged_in)
        else:
            print("Access Denied! Please login first.")
    return wrapper

@login_required
def view_profile(is_logged_in):
    print("Welcome! You can access your profile.")


# -------------------------------
# 2. Function Call Logger
# -------------------------------
def log_function(func):
    def wrapper():
        print("Function Name:", func.__name__)
        print("Called At:", datetime.now())
        return func()
    return wrapper

@log_function
def display_message():
    print("Hello! This is a sample function.")


# -------------------------------
# 3. Input Validation
# -------------------------------
def validate_positive(func):
    def wrapper(*args):
        for value in args:
            if not isinstance(value, int) or value <= 0:
                print("Error: All arguments must be positive integers.")
                return
        return func(*args)
    return wrapper

@validate_positive
def multiply(a, b):
    print("Product =", a * b)


# ==========================================
# 4. Function Call Counter
# ==========================================

def count_calls(original_function):
    total_calls = 0

    def execute():
        nonlocal total_calls
        total_calls += 1
        print(f"\nFunction executed {total_calls} time(s).")
        return original_function()

    return execute


@count_calls
def welcome_user():
    print("Welcome to the Sales Management System!")


# -------------------------------
# Main Program
# -------------------------------
print("1. Login Authentication")
view_profile(True)
view_profile(False)

print("\n2. Function Logger")
display_message()

print("\n3. Input Validation")
multiply(5, 6)
multiply(5, -2)

print("\n----- Function Call Counter -----")
welcome_user()
welcome_user()
welcome_user()