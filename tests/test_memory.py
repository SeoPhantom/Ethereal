
# tests/test_memory.py
"""
Ensures memory management works correctly.
"""
from openmeta.core.memory import Memory

def test_memory():
    memory = Memory()
    memory.store("Test data")
    assert "Test data" in memory.retrieve()

test_memory()
