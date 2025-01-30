import logging
from web3 import Web3
from typing import Optional

# Configure logging system
logging.basicConfig(
    filename="ethereal_sdk.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BlockchainConnector:
    def __init__(self, network: str, provider_url: Optional[str] = None):
        """Initializes the BlockchainConnector with network and optional provider URL."""
        if not isinstance(network, str) or not network.strip():
            logging.error("Invalid network name provided.")
            raise ValueError("Network must be a non-empty string.")
        
        self.network = network
        self.provider_url = provider_url or self.get_provider_url(network)
        logging.info(f"Blockchain connector initialized for {self.network}.")

    def get_provider_url(self, network: str) -> str:
        """Returns the appropriate provider URL based on the network."""
        # Add more networks as required
        if network.lower() == "ethereum":
            return "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
        elif network.lower() == "binance":
            return "https://bsc-dataseed.binance.org/"
        else:
            raise ValueError(f"Unsupported network: {network}")

    def connect(self) -> str:
        """Establishes a connection to the blockchain network."""
        try:
            # Initialize Web3 connection
            web3 = Web3(Web3.HTTPProvider(self.provider_url))
            
            # Check if the connection is successful
            if not web3.isConnected():
                logging.error(f"Failed to connect to {self.network} network.")
                raise ConnectionError(f"Unable to connect to {self.network} blockchain.")
            
            logging.info(f"Successfully connected to {self.network} blockchain.")
            return f"Connected to {self.network} blockchain"
        except Exception as e:
            logging.error(f"Error connecting to {self.network} blockchain: {e}")
            raise RuntimeError(f"Failed to connect to {self.network} blockchain: {e}")
