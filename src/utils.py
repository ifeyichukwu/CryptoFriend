# utils.py

# Helper functions for the chatbot

def fetch_crypto_data(crypto_name):
    # Mockup data for testing
    mock_data = {
        "Bitcoin": {
            "current_price": 50000,
            "7_day_trend": "up",
            "volatility": 0.03,
            "consensus_mechanism": "PoW",
            "energy_consumption": "High",
            "project_maturity": "Established"
        },
        "Ethereum": {
            "current_price": 4000,
            "7_day_trend": "down",
            "volatility": 0.05,
            "consensus_mechanism": "PoS",
            "energy_consumption": "Medium",
            "project_maturity": "Emerging"
        }
    }
    return mock_data.get(crypto_name, None) 