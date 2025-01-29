# openmeta/core/agent.py
"""
Defines the main Agent class and its behavior.
"""
class Agent:
    def __init__(self, name, memory):
        self.name = name
        self.memory = memory
    
    def process_task(self, task):
        """Processes a task and stores it in memory."""
        result = f"Processing task: {task}"
        self.memory.store(result)
        return result