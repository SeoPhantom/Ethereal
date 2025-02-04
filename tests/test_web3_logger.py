import unittest
from unittest.mock import patch, MagicMock
from web3 import Web3
from openmeta.core.web3_logger import log_to_blockchain, retrieve_log
from openmeta.config.settings import Settings

class TestWeb3Logger(unittest.TestCase):

    def setUp(self):
        """Setup environment before each test."""
        # Mock settings for Web3
        self.settings = Settings()
        self.settings.set("use_web3_logging", True)
        self.settings.set("network", "ethereum")
        self.settings.set("web3_provider_url", "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID")

    @patch('src.web3_logger.Web3')
    def test_log_to_blockchain(self, MockWeb3):
        """Test if logs are being sent to the blockchain."""
        
        # Arrange: Mock Web3 connection and transaction
        mock_web3_instance = MagicMock()
        mock_web3_instance.eth.sendTransaction.return_value = '0x123abc'
        MockWeb3.return_value = mock_web3_instance

        agent_id = "agent_1"
        action = "perform_action"
        
        # Act: Call the log_to_blockchain function
        result = log_to_blockchain(agent_id, action)
        
        # Assert: Verify that the log was sent to the blockchain
        mock_web3_instance.eth.sendTransaction.assert_called_once()
        self.assertEqual(result, "Action logged to blockchain successfully.")
    
    @patch('src.web3_logger.Web3')
    def test_retrieve_log(self, MockWeb3):
        """Test if logs can be retrieved from the blockchain."""
        
        # Arrange: Mock Web3 connection and response for retrieving log
        mock_web3_instance = MagicMock()
        mock_web3_instance.eth.getLogs.return_value = [{"logIndex": 1, "agent_id": "agent_1", "action": "perform_action"}]
        MockWeb3.return_value = mock_web3_instance

        agent_id = "agent_1"
        
        # Act: Call the retrieve_log function
        logs = retrieve_log(agent_id)
        
        # Assert: Verify that logs are correctly retrieved
        mock_web3_instance.eth.getLogs.assert_called_once_with({'fromBlock': 0, 'toBlock': 'latest', 'filter': {'agent_id': agent_id}})
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0]['action'], "perform_action")
    
    def test_no_web3_logging_enabled(self):
        """Test when Web3 logging is not enabled in the settings."""
        self.settings.set("use_web3_logging", False)
        
        agent_id = "agent_1"
        action = "perform_action"
        
        # Act: Call the log_to_blockchain function when Web3 logging is disabled
        result = log_to_blockchain(agent_id, action)
        
        # Assert: Verify that the action was not logged since Web3 logging is disabled
        self.assertEqual(result, "Web3 logging is disabled.")
        
    def test_invalid_network_configuration(self):
        """Test if the network configuration is invalid."""
        self.settings.set("network", "invalid_network")
        
        agent_id = "agent_1"
        action = "perform_action"
        
        # Act: Call the log_to_blockchain function with an invalid network
        with self.assertRaises(ValueError):
            log_to_blockchain(agent_id, action)

if __name__ == '__main__':
    unittest.main()
