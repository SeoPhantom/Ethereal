import logging

logging.basicConfig(
    filename="ethereal_sdk.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Settings:
    def __init__(self):
        """Initializes the configuration with default settings."""
        self.config = {
            "log_level": "INFO",
            "use_blockchain": False,
            "use_web3_logging": False,  # New config for enabling/disabling Web3 logging
            "api_key": "your_api_key_here",
            "network": "ethereum",  # Default network for Web3
            "web3_provider_url": "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Default provider URL
        }
        logging.info("Settings initialized with default configuration.")

    def get(self, key: str):
        """Fetches a configuration value by key."""
        if key not in self.config:
            logging.error(f"Attempted to fetch non-existing configuration key: {key}")
            raise KeyError(f"Configuration key '{key}' not found.")
        
        logging.info(f"Retrieved configuration value for key: {key}")
        return self.config.get(key)

    def set(self, key: str, value):
        """Sets a configuration value by key."""
        if not isinstance(key, str) or not key.strip():
            logging.error("Invalid key provided for setting configuration.")
            raise ValueError("Configuration key must be a non-empty string.")
        
        if key == "log_level" and value not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            logging.error(f"Invalid log level value provided: {value}")
            raise ValueError(f"Invalid log level: {value}. Must be one of ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'].")
        
        if key == "use_web3_logging" and not isinstance(value, bool):
            logging.error(f"Invalid value for 'use_web3_logging': {value}. Must be a boolean.")
            raise ValueError("'use_web3_logging' must be a boolean value.")
        
        self.config[key] = value
        logging.info(f"Configuration updated for key: {key} with value: {value}")
