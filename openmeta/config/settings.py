# openmeta/config/settings.py
"""
Manages global configuration and settings.
"""
class Settings:
    def __init__(self):
        self.config = {
            "log_level": "INFO",
            "use_blockchain": False,
            "api_key": "your_api_key_here"
        }
    
    def get(self, key):
        return self.config.get(key)
    
    def set(self, key, value):
        self.config[key] = value
