import logging
from typing import Dict, Any
from openmeta.core.agent_customization import AgentCustomization  # Import the customization class
from openmeta.core.task_queue import TaskQueue, TaskQueueError  # Import your task queue system and custom error

# Configure logging system
logging.basicConfig(level=logging.INFO)

class Agent:
    def __init__(self, name: str):
        self.name = name
        self.task_queue = TaskQueue()  # Initialize TaskQueue
        self.customization = AgentCustomization(self)

    def add_task(self, task: Dict[str, Any]):
        """Add a new task to the task queue with validation and error handling."""
        try:
            # Validate task data
            if not self._validate_task(task):
                raise ValueError("Invalid task data. Task is missing required fields.")

            logging.info(f"Adding task {task.get('id')} to queue")
            self.task_queue.add_to_queue(task)  # Add task to the queue

        except ValueError as e:
            logging.error(f"Task validation failed: {e}")
        except TaskQueueError as e:
            logging.error(f"Failed to add task to queue: {e}")
        except Exception as e:
            logging.error(f"Unexpected error while adding task: {e}")

    def process_tasks(self):
        """Process tasks from the queue asynchronously."""
        try:
            logging.info("Starting to process tasks...")
            self.task_queue.process_queue()  # Process the queue
            logging.info("Task processing complete.")
        except TaskQueueError as e:
            logging.error(f"Error processing tasks: {e}")
        except Exception as e:
            logging.error(f"Unexpected error during task processing: {e}")

    def _validate_task(self, task: Dict[str, Any]) -> bool:
        """Validate the structure and content of a task."""
        required_fields = ['id', 'priority', 'task_type']
        for field in required_fields:
            if field not in task:
                logging.warning(f"Missing required field: {field}")
                return False
        return True
