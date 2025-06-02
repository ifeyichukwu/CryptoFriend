# utils.py

# Helper functions for the chatbot

def fetch_crypto_data(crypto_name):
    # Updated mock data for testing
    crypto_db = {
        "Bitcoin": {
            "price_trend": "rising",
            "market_cap": "high",
            "energy_use": "high",
            "sustainability_score": 3/10
        },
        "Ethereum": {
            "price_trend": "stable",
            "market_cap": "high",
            "energy_use": "medium",
            "sustainability_score": 6/10
        },
        "Cardano": {
            "price_trend": "rising",
            "market_cap": "medium",
            "energy_use": "low",
            "sustainability_score": 8/10
        }
    }
    return crypto_db.get(crypto_name, None) 