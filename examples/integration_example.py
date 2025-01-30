import logging
from openmeta.integrations.external_api import ExternalAPI
from openmeta.integrations.blockchain import BlockchainConnector

logging.basicConfig(
    filename="ethereal_sdk_example.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    try:
        api = ExternalAPI("https://example.com/api", api_key="your_api_key_here")
        endpoint = "/test-endpoint"
        logging.info(f"Fetching data from API endpoint: {endpoint}")
        api_response = api.fetch_data(endpoint)
        print(f"API Response: {api_response}")
        logging.info("API data fetched successfully.")

        blockchain = BlockchainConnector("Ethereum")
        logging.info(f"Connecting to blockchain: Ethereum")
        blockchain_response = blockchain.connect()
        print(f"Blockchain Connection: {blockchain_response}")
        logging.info("Blockchain connected successfully.")

    except Exception as e:
        logging.error(f"Error in integration example: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
