# openmeta/utils/logging_utils.py
"""
Provides logging enhancements.
"""
class Logger:
    def __init__(self, level="INFO"):
        self.level = level
    
    def log(self, message):
        """Logs a message at the specified level."""
        return f"[{self.level}] {message}"
