# openmeta/core/memory.py
"""
Handles agent memory operations.
"""
class Memory:
    def __init__(self):
        self.storage = []
    
    def store(self, data):
        """Stores data in memory."""
        self.storage.append(data)
    
    def retrieve(self, index=None):
        """Retrieves stored data. If index is provided, returns specific entry."""
        return self.storage if index is None else self.storage[index]
