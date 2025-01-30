import logging
from typing import Union

# Configure logging system
logging.basicConfig(
    filename="ethereal_sdk.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Memory:
    def __init__(self):
        self.storage = []
        logging.info("Memory initialized.")
    
    def store(self, data: Union[str, None]):
        """Stores data in memory."""
        if not isinstance(data, str) or not data.strip():
            logging.error("Invalid data format received for storing.")
            raise ValueError("Data must be a non-empty string.")
        
        try:
            self.storage.append(data)
            logging.info(f"Data stored successfully: {data}")
        except Exception as e:
            logging.error(f"Error storing data: {e}")
            raise RuntimeError(f"Failed to store data: {e}")
    
    def retrieve(self, index: Union[int, None] = None):
        """Retrieves stored data. If index is provided, returns specific entry."""
        if index is not None and (not isinstance(index, int) or index < 0 or index >= len(self.storage)):
            logging.error(f"Invalid index provided: {index}")
            raise IndexError("Index out of range.")
        
        try:
            if index is None:
                return self.storage
            return self.storage[index]
        except Exception as e:
            logging.error(f"Error retrieving data at index {index}: {e}")
            raise RuntimeError(f"Failed to retrieve data at index {index}: {e}")
