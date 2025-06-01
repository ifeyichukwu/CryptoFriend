# main.py

from src.chatbot import Chatbot

def main():
    print("Welcome to CryptoFriend Chatbot!")
    chatbot = Chatbot()
    
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = chatbot.handle_query(query)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main() 