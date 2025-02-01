import logging
import re
from typing import Union
from openmeta.core.agent_customization import AgentCustomization  # Import the customization class

# Configure logging system
logging.basicConfig(
    filename="ethereal_sdk.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Agent:
    def __init__(self, name: str, memory, customization: AgentCustomization = None):
        """
        Initializes an agent with a name, memory, and optional customization.

        :param name: The name of the agent
        :param memory: The memory object where agent data will be stored
        :param customization: The customization object for adjusting agent behavior (optional)
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Agent name must be a non-empty string.")
        
        self.name = name
        self.memory = memory
        self.customization = customization  # Support for customization functionality

        logging.info(f"Agent '{self.name}' initialized.")

    def process_task(self, task: Union[str, None]) -> str:
        """Processes a task, applies customizations, and stores it in memory."""
        
        # Validate task input
        if not isinstance(task, str) or not re.match(r"^[a-zA-Z0-9\s]+$", task):
            logging.error("Invalid task format received.")
            raise ValueError("Task must be a non-empty string containing only letters, numbers, and spaces.")
        
        # Apply customizations if provided
        if self.customization:
            try:
                customizations = self.customization.get_current_customizations(self.name)
                logging.info(f"Using customizations: {customizations}")
                # Example: Adjust task processing based on customization
                task_priority = customizations.get("task_priority", "normal")
                logging.info(f"Task priority set to: {task_priority}")
            except KeyError:
                logging.info(f"No customizations found for agent {self.name}")

        try:
            # Process the task
            result = f"Processing task: {task}"
            self.memory.store(result)
            
            logging.info(f"Task processed successfully: {task}")
            return result
        except Exception as e:
            # Log error
            logging.error(f"Error processing task '{task}': {e}")
            raise RuntimeError(f"Failed to process task: {e}")
