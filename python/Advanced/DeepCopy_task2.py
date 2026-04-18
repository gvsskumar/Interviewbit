# Write a custom deep copy function (without using copy.deepcopy).
def custom_deepcopy(obj):
    # Handle immutable types directly
    if isinstance(obj, (int, float, str, bool, type(None))):
        return obj

    # Handle list
    if isinstance(obj, list):
        return [custom_deepcopy(item) for item in obj]

    # Handle tuple
    if isinstance(obj, tuple):
        return tuple(custom_deepcopy(item) for item in obj)

    # Handle set
    if isinstance(obj, set):
        return {custom_deepcopy(item) for item in obj}

    # Handle dict
    if isinstance(obj, dict):
        return {
            custom_deepcopy(key): custom_deepcopy(value)
            for key, value in obj.items()
        }

    # Fallback (for unsupported types)
    return obj