
# examples/minimal_agent.py
"""
Simple example to create an agent.
"""
from openmeta.core.agent import Agent
from openmeta.core.memory import Memory

if __name__ == "__main__":
    memory = Memory()
    agent = Agent("TestAgent", memory)
    print(agent.process_task("Analyze data stream"))
