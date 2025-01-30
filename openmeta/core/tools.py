import logging
from typing import Any, Tuple

# Configure logging system
logging.basicConfig(
    filename="ethereal_sdk.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Tool:
    def __init__(self, tool_name: str):
        """Initializes the Tool with a name."""
        if not isinstance(tool_name, str) or not tool_name.strip():
            logging.error("Invalid tool name provided.")
            raise ValueError("Tool name must be a non-empty string.")
        
        self.tool_name = tool_name
        logging.info(f"Tool '{self.tool_name}' initialized.")
    
    def execute(self, *args: Tuple[Any], **kwargs: dict) -> str:
        """Executes an external tool with the given arguments."""
        # Validate input arguments
        if not all(isinstance(arg, (str, int, float, bool)) for arg in args):
            logging.error(f"Invalid argument types passed to tool: {args}")
            raise TypeError("Arguments must be of type str, int, float, or bool.")
        
        if not all(isinstance(value, (str, int, float, bool)) for value in kwargs.values()):
            logging.error(f"Invalid keyword argument types passed to tool: {kwargs}")
            raise TypeError("Keyword arguments must be of type str, int, float, or bool.")
        
        try:
            # Simulate tool execution
            result = f"{self.tool_name} executed with {args} and {kwargs}"
            logging.info(f"Tool execution successful: {self.tool_name} with {args} and {kwargs}")
            return result
        except Exception as e:
            logging.error(f"Error executing tool '{self.tool_name}' with args {args} and kwargs {kwargs}: {e}")
            raise RuntimeError(f"Failed to execute tool '{self.tool_name}': {e}")
