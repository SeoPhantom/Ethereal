import logging
from typing import Callable, List, Any

# Configure logging system
logging.basicConfig(
    filename="ethereal_sdk.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Workflow:
    def __init__(self, steps: List[Callable[[], Any]]):
        """Initializes the workflow with a list of steps."""
        if not isinstance(steps, list) or not all(callable(step) for step in steps):
            logging.error("Invalid steps provided for workflow.")
            raise ValueError("Steps must be a list of callable functions.")
        
        self.steps = steps
        logging.info("Workflow initialized with steps.")

    def execute(self) -> List[Any]:
        """Executes the workflow steps in sequence."""
        results = []
        
        for i, step in enumerate(self.steps, 1):
            try:
                logging.info(f"Executing step {i}...")
                result = step()
                results.append(result)
                logging.info(f"Step {i} executed successfully: {result}")
            except Exception as e:
                logging.error(f"Error executing step {i}: {e}")
                raise RuntimeError(f"Workflow failed at step {i}: {e}")
        
        return results
