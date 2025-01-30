import logging
from openmeta.core.agent import Agent
from openmeta.core.memory import Memory

logging.basicConfig(
    filename="ethereal_sdk_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def test_agent():
    try:
        memory = Memory()
        agent = Agent("TestAgent", memory)
        
        task = "Unit test task"
        logging.info(f"Running test with task: {task}")
        
        result = agent.process_task(task)
        
        assert "Unit test task" in result, f"Test failed. Expected to find '{task}' in the result."
        
        logging.info(f"Test passed. Task '{task}' processed successfully.")

    except AssertionError as e:
        logging.error(f"AssertionError: {e}")
        print(f"AssertionError: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    test_agent()
