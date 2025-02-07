# tests/test_error_handler.py

import unittest
from unittest.mock import patch
from openmeta.utils.error_handler import handle_error, fallback_action
from openmeta.core.task_queue import TaskQueueError
from openmeta.utils.error_handler import retry_task


class TestErrorHandler(unittest.TestCase):
    """Test suite for error handling and fallback mechanisms."""

    @patch('src.utils.error_handler.logger')
    def test_handle_error_value_error(self, mock_logger):
        """Test if ValueError is handled correctly and logs the error."""
        # Simulate a ValueError scenario
        exception = ValueError("Invalid task data")
        agent_id = "agent_1"
        
        handle_error(exception, agent_id)
        
        # Check if the correct log message is generated
        mock_logger.error.assert_called_with(f"Error encountered in agent {agent_id}: {exception}")
        mock_logger.warning.assert_called_with("Connection error for agent agent_1. Attempting to reconnect...")
    
    @patch('src.utils.error_handler.logger')
    def test_handle_error_task_queue_error(self, mock_logger):
        """Test if TaskQueueError is handled correctly and logs the error."""
        exception = TaskQueueError("Task queue failure")
        agent_id = "agent_2"
        
        handle_error(exception, agent_id)
        
        # Check if the correct log message is generated
        mock_logger.error.assert_called_with(f"Error encountered in agent {agent_id}: {exception}")
        mock_logger.warning.assert_called_with(f"Connection error for agent {agent_id}. Attempting to reconnect...")
    
    @patch('src.utils.error_handler.logger')
    def test_handle_error_generic_exception(self, mock_logger):
        """Test if a generic exception is handled and logged."""
        exception = Exception("Some unexpected error")
        agent_id = "agent_3"
        
        handle_error(exception, agent_id)
        
        # Check if the correct log message is generated
        mock_logger.error.assert_called_with(f"Error encountered in agent {agent_id}: {exception}")
        mock_logger.critical.assert_called_with(f"Critical error for agent {agent_id}. Manual intervention may be required.")
    
    @patch('src.utils.error_handler.retry_task')
    @patch('src.utils.error_handler.logger')
    def test_fallback_action_retry(self, mock_logger, mock_retry_task):
        """Test the fallback action for retrying tasks."""
        agent_id = "agent_4"
        
        fallback_action(agent_id)
        
        # Check if retry_task was called
        mock_retry_task.assert_called_with(agent_id)
        mock_logger.info.assert_called_with(f"Performing fallback actions for agent {agent_id}.")
    
    @patch('src.utils.error_handler.logger')
    def test_retry_task(self, mock_logger):
        """Test the retry_task functionality."""
        agent_id = "agent_5"
        
        retry_task(agent_id)
        
        # Check if the correct log message is generated
        mock_logger.info.assert_called_with(f"Retrying task for agent {agent_id}...")

if __name__ == '__main__':
    unittest.main()
