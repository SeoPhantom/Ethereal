import logging
from openmeta.core.workflows import Workflow

logging.basicConfig(
    filename="ethereal_sdk_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def step():
    logging.info("Executing step: Step executed")
    return "Step executed"

def test_workflow():
    try:
        workflow = Workflow([step, step])
        
        logging.info("Starting workflow execution.")
        results = workflow.execute()
        
        expected_results = ["Step executed", "Step executed"]
        assert results == expected_results, f"Test failed. Expected {expected_results} but got {results}"
        
        logging.info("Test passed. Workflow executed successfully with results: %s", results)
    
    except AssertionError as e:
        logging.error(f"AssertionError: {e}")
        print(f"AssertionError: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    test_workflow()
