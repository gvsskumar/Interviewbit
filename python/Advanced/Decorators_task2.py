#Challenge 2: Authentication Decorator
def require_login(func):
    def wrapper(user):
        if not user.get("is_logged_in"):
            return "Access Denied"
        return func(user)
    return wrapper

@require_login
def dashboard(user):
    return "Welcome!"

print(dashboard({"is_logged_in": True}))