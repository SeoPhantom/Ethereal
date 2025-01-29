# openmeta/utils/validators.py
"""
Validates inputs and outputs for agents.
"""
class Validator:
    @staticmethod
    def validate_data(data):
        """Validates if input data is a dictionary."""
        if isinstance(data, dict):
            return True
        raise ValueError("Invalid data format. Expected a dictionary.")
