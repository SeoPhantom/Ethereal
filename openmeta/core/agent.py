import logging
import re
from typing import Union

# Configure logging system
logging.basicConfig(
    filename="ethereal_sdk.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Agent:
    def __init__(self, name: str, memory):
        # Validate name
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Agent name must be a non-empty string.")
        
        self.name = name
        self.memory = memory
        
        logging.info(f"Agent '{self.name}' initialized.")
    
    def process_task(self, task: Union[str, None]) -> str:
        """Processes a task, validates input, and stores it in memory."""
        
        # Validate task input
        if not isinstance(task, str) or not re.match(r"^[a-zA-Z0-9\s]+$", task):
            logging.error("Invalid task format received.")
            raise ValueError("Task must be a non-empty string containing only letters, numbers, and spaces.")
        
        try:
            # Process task
            result = f"Processing task: {task}"
            self.memory.store(result)
            
            logging.info(f"Task processed successfully: {task}")
            return result
        except Exception as e:
            # Log error
            logging.error(f"Error processing task '{task}': {e}")
            raise RuntimeError(f"Failed to process task: {e}")
