import logging
import requests
from typing import Optional, Dict

# Configure logging system
logging.basicConfig(
    filename="ethereal_sdk.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ExternalAPI:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """Initializes the API connector with a base URL and optional API key."""
        if not isinstance(base_url, str) or not base_url.strip():
            logging.error("Invalid base URL provided.")
            raise ValueError("Base URL must be a non-empty string.")
        
        self.base_url = base_url
        self.api_key = api_key
        logging.info(f"ExternalAPI initialized for {self.base_url}")

    def fetch_data(self, endpoint: str, params: Optional[Dict[str, str]] = None) -> Dict:
        """Fetches data from an external API endpoint."""
        if not isinstance(endpoint, str) or not endpoint.strip():
            logging.error("Invalid endpoint provided.")
            raise ValueError("Endpoint must be a non-empty string.")
        
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=5)
            response.raise_for_status()  # Will raise an exception for HTTP errors
            logging.info(f"Data fetched successfully from {url}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data from {url}: {e}")
            raise RuntimeError(f"Failed to fetch data from {url}: {e}")
