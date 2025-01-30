import logging
from openmeta.core.agent import Agent
from openmeta.core.memory import Memory

logging.basicConfig(
    filename="ethereal_sdk_example.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    try:
        memory = Memory()
        agent = Agent("TestAgent", memory)
        
        task = "Analyze data stream"
        logging.info(f"Processing task: {task}")
        
        result = agent.process_task(task)
        
        print(f"Task Result: {result}")
        logging.info(f"Task completed successfully: {result}")
    
    except ValueError as e:
        logging.error(f"ValueError occurred: {e}")
        print(f"Input Error: {e}")
    except RuntimeError as e:
        logging.error(f"RuntimeError occurred: {e}")
        print(f"Runtime Error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
