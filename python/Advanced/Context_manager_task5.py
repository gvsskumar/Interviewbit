# Build a context manager that temporarily changes environment variables.
import os

class TempEnv:
    def __init__(self, **env_vars):
        self.new_env = env_vars
        self.old_env = {}

    def __enter__(self):
        # Save old values and set new ones
        for key, value in self.new_env.items():
            self.old_env[key] = os.environ.get(key)
            os.environ[key] = str(value)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Restore original values
        for key, old_value in self.old_env.items():
            if old_value is None:
                os.environ.pop(key, None)  # remove if not originally present
            else:
                os.environ[key] = old_value