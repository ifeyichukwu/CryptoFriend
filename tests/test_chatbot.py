# test_chatbot.py

import unittest
from src.chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = Chatbot()

    def test_handle_query(self):
        # Test the handle_query method
        self.assertIsNotNone(self.chatbot.handle_query("Should I invest in Bitcoin?"))

if __name__ == "__main__":
    unittest.main() 