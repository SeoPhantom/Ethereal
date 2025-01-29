# tests/test_agent.py
"""
Tests the Agent class functionality.
"""
from openmeta.core.agent import Agent
from openmeta.core.memory import Memory

def test_agent():
    memory = Memory()
    agent = Agent("TestAgent", memory)
    result = agent.process_task("Unit test task")
    assert "Unit test task" in result

test_agent()