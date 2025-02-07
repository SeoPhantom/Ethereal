# src/utils/error_handler.py

import logging
from typing import Optional

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def handle_error(exception: Exception, agent_id: Optional[str] = None):
    """
    Handles errors by logging them and executing fallback actions.
    
    Args:
        exception (Exception): The exception to be logged.
        agent_id (Optional[str]): ID of the agent that encountered the error (default is None).
    """
    # Log the error with the appropriate severity
    logger.error(f"Error encountered in agent {agent_id if agent_id else 'Unknown'}: {exception}")
    
    # Define fallback action based on the type or severity of the error
    if isinstance(exception, ConnectionError):
        logger.warning(f"Connection error for agent {agent_id}. Attempting to reconnect...")
        fallback_action(agent_id)
    elif isinstance(exception, TimeoutError):
        logger.warning(f"Timeout error for agent {agent_id}. Retrying the task...")
        fallback_action(agent_id)
    else:
        logger.critical(f"Critical error for agent {agent_id}. Manual intervention may be required.")
        # Handle any critical fallback actions if needed
        fallback_action(agent_id)

def fallback_action(agent_id: Optional[str] = None):
    """
    Executes predefined fallback actions, such as retrying a task or switching to a backup agent.
    
    Args:
        agent_id (Optional[str]): ID of the agent that encountered the error (default is None).
    """
    # Example fallback actions: retrying the task or switching to a backup agent
    if agent_id:
        logger.info(f"Performing fallback actions for agent {agent_id}.")
        # You can implement custom retry logic or backup agent logic here
        retry_task(agent_id)
    else:
        logger.warning("No agent ID provided for fallback action.")

def retry_task(agent_id: str):
    """
    Retry the task assigned to the agent.
    
    Args:
        agent_id (str): ID of the agent whose task will be retried.
    """
    # Example of retrying the task
    logger.info(f"Retrying task for agent {agent_id}...")
    # Add your retry logic here
