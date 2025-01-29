# openmeta/core/workflows.py
"""
Implements workflow patterns inspired by Anthropic.
"""
class Workflow:
    def __init__(self, steps):
        self.steps = steps
    
    def execute(self):
        """Executes the workflow steps in sequence."""
        results = []
        for step in self.steps:
            results.append(step())
        return results
