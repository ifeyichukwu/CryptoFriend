# chatbot.py

from src.utils import fetch_crypto_data

class Chatbot:
    def __init__(self):
        pass

    def handle_query(self, query):
        if "invest in" in query:
            crypto_name = query.split("invest in")[-1].strip()
            data = fetch_crypto_data(crypto_name)
            if data:
                return self.analyze_investment(data)
            else:
                return "Sorry, I couldn't fetch data for that cryptocurrency."

    def analyze_investment(self, data):
        # Analyze profitability and sustainability
        profitability = self.analyze_profitability(data)
        sustainability = self.analyze_sustainability(data)
        return f"📈 Profitability Analysis: {profitability}\n🌱 Sustainability Analysis: {sustainability}\n✅ Investment Verdict: High Potential"
    
    def analyze_profitability(self, data):
        # Implement profitability analysis logic
        return "Profitable"

    def analyze_sustainability(self, data):
        # Implement sustainability analysis logic
        return "Sustainable" 