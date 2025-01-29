# tests/test_workflows.py
"""
Tests workflow implementations and patterns.
"""
from openmeta.core.workflows import Workflow

def step():
    return "Step executed"

def test_workflow():
    workflow = Workflow([step, step])
    results = workflow.execute()
    assert results == ["Step executed", "Step executed"]

test_workflow()