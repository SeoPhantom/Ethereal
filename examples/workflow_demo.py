import logging
from openmeta.core.workflows import Workflow

logging.basicConfig(
    filename="ethereal_sdk_example.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def step1():
    logging.info("Executing Step 1: Data preprocessing")
    return "Step 1: Data preprocessing"

def step2():
    logging.info("Executing Step 2: Model training")
    return "Step 2: Model training"

def step3():
    logging.info("Executing Step 3: Evaluation")
    return "Step 3: Evaluation"

def main():
    try:
        # Create workflow with steps
        steps = [step1, step2, step3]
        workflow = Workflow(steps)

        # Execute the workflow and print results
        logging.info("Starting workflow execution.")
        result = workflow.execute()
        logging.info(f"Workflow execution completed successfully: {result}")
        print(result)

    except Exception as e:
        logging.error(f"Error during workflow execution: {e}")
        print(f"An error occurred during the workflow: {e}")

if __name__ == "__main__":
    main()
