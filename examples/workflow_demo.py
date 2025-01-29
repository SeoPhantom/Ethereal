# examples/workflow_demo.py
"""
Demonstrates advanced workflow patterns.
"""
from openmeta.core.workflows import Workflow

def step1():
    return "Step 1: Data preprocessing"

def step2():
    return "Step 2: Model training"

def step3():
    return "Step 3: Evaluation"

if __name__ == "__main__":
    workflow = Workflow([step1, step2, step3])
    print(workflow.execute())