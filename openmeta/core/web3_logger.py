import logging
from openmeta.integrations.blockchain import BlockchainConnector
from web3 import Web3
from typing import Optional

# Configure logging system
logging.basicConfig(
    filename="ethereal_sdk.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Web3Logger:
    def __init__(self, network: str, provider_url: Optional[str] = None):
        """Initialize Web3Logger with a blockchain connection."""
        self.blockchain_connector = BlockchainConnector(network, provider_url)
        self.web3 = Web3(Web3.HTTPProvider(self.blockchain_connector.provider_url))
        if not self.web3.isConnected():
            logging.error(f"Failed to connect to the blockchain at {provider_url}.")
            raise ConnectionError("Blockchain is not connected.")
        logging.info(f"Web3Logger initialized for {network} network.")

    def log_to_blockchain(self, agent_id: str, action: str):
        """Log the agent action to the blockchain."""
        try:
            if not agent_id:
                raise ValueError("Agent ID is required.")
            if not action:
                raise ValueError("Action is required.")

            log_data = f"Agent {agent_id} performed action: {action}"

            # Construct the transaction
            transaction = {
                'to': '0xYourContractAddress',  # Replace with contract address
                'from': self.web3.eth.accounts[0],  # Use a proper wallet address
                'data': self.web3.toHex(text=log_data)
            }

            # Send the transaction
            tx_hash = self.web3.eth.sendTransaction(transaction)
            logging.info(f"Log action sent to blockchain: {log_data} with TX hash: {tx_hash.hex()}")
            return tx_hash

        except ValueError as ve:
            logging.error(f"Input validation error: {ve}")
            raise
        except Exception as e:
            logging.error(f"Error logging action to blockchain: {e}")
            raise

    def retrieve_log(self, agent_id: str) -> str:
        """Retrieve the agent's action logs from the blockchain."""
        try:
            if not agent_id:
                raise ValueError("Agent ID is required.")

            # Retrieve logs filtered by agent_id
            logs = self.web3.eth.getLogs({
                'fromBlock': 0,
                'toBlock': 'latest',
                'address': '0xYourContractAddress',  # Replace with your contract address
                'topics': [self.web3.sha3(text=f'Agent {agent_id}')]  # Filter by agent_id
            })

            if logs:
                log_data = self.web3.toText(logs[0]['data'])  # Decode log data from 'data'
                logging.info(f"Retrieved log: {log_data}")
                return log_data
            else:
                logging.warning(f"No logs found for agent {agent_id}")
                return "No logs found."

        except ValueError as ve:
            logging.error(f"Input validation error: {ve}")
            raise
        except Exception as e:
            logging.error(f"Error retrieving logs from blockchain: {e}")
            raise
