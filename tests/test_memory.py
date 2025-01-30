import logging
from openmeta.core.memory import Memory

logging.basicConfig(
    filename="ethereal_sdk_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def test_memory():
    try:
        memory = Memory()
        
        data = "Test data"
        logging.info(f"Storing data: {data}")
        
        memory.store(data)
        retrieved_data = memory.retrieve()
        assert data in retrieved_data, f"Test failed. Expected '{data}' to be in the retrieved data."
        
        logging.info(f"Test passed. Data '{data}' successfully stored and retrieved.")

    except AssertionError as e:
        logging.error(f"AssertionError: {e}")
        print(f"AssertionError: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    test_memory()
