# examples/integration_example.py
"""
Shows integration with APIs and blockchain.
"""
from openmeta.integrations.external_api import ExternalAPI
from openmeta.integrations.blockchain import BlockchainConnector

if __name__ == "__main__":
    api = ExternalAPI("https://example.com/api")
    print(api.fetch_data("/test-endpoint"))
    
    blockchain = BlockchainConnector("Ethereum")
    print(blockchain.connect())