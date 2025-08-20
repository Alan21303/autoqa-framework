import os

# Example config values (expand later when needed)
BASE_URL = "https://the-internet.herokuapp.com"

def get_env(var_name: str, default=None):
    """Helper to read environment variables with fallback."""
    return os.getenv(var_name, default)
