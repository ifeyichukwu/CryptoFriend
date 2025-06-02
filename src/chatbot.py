# chatbot.py

from src.utils import fetch_crypto_data

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

class Chatbot:
    def __init__(self):
        pass

    def handle_query(self, query):
        query = query.lower()
        if "invest in" in query:
            crypto_name = query.split("invest in")[-1].strip()
            data = fetch_crypto_data(crypto_name)
            if data:
                return self.analyze_investment(data)
            else:
                return f"Sorry, I couldn't fetch data for {crypto_name}."
        elif "trending up" in query:
            trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
            return f"These cryptocurrencies are trending up: {', '.join(trending)}. 📈"
        elif "sustainable" in query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            return f"Invest in {recommend}! 🌱 It's eco-friendly and has long-term potential!"
        elif "market cap" in query:
            high_cap = [name for name, data in crypto_db.items() if data["market_cap"] == "high"]
            return f"These cryptocurrencies have a high market cap: {', '.join(high_cap)}. 💰"
        elif "energy use" in query:
            low_energy = [name for name, data in crypto_db.items() if data["energy_use"] == "low"]
            return f"These cryptocurrencies have low energy use: {', '.join(low_energy)}. ⚡"
        else:
            return "I'm not sure how to respond to that. Please ask about investing in a specific cryptocurrency or inquire about trends, sustainability, market cap, or energy use."

    def analyze_profitability(self, data):
        # Assess profitability based on price trend and market cap
        trend = data["price_trend"]
        market_cap = data["market_cap"]
        
        if trend == "rising" and market_cap == "high":
            return "High Profitability"
        elif trend == "stable" and market_cap == "medium":
            return "Moderate Profitability"
        else:
            return "Low Profitability"

    def analyze_sustainability(self, data):
        # Assess sustainability based on energy use and sustainability score
        energy_use = data["energy_use"]
        sustainability_score = data["sustainability_score"]
        
        if energy_use == "low" and sustainability_score > 7:
            return "Highly Sustainable"
        elif energy_use == "high" and sustainability_score < 4:
            return "Not Sustainable"
        else:
            return "Moderately Sustainable"

    def analyze_investment(self, data):
        # Combine profitability and sustainability analyses
        profitability = self.analyze_profitability(data)
        sustainability = self.analyze_sustainability(data)
        
        if profitability == "High Profitability" and sustainability == "Highly Sustainable":
            verdict = "High Potential"
        elif profitability == "Not Profitable" or sustainability == "Not Sustainable":
            verdict = "Unsustainable"
        else:
            verdict = "Moderate Risk"
        
        return f"📈 Profitability Analysis: {profitability}\n🌱 Sustainability Analysis: {sustainability}\n✅ Investment Verdict: {verdict}" 