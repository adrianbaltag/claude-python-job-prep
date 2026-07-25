class ChatBot:
    def __init__(self, client, system):
        self.client = client
        self.system = system
        self.conversation_history = []


my_bot = ChatBot("fake_client", "grumpy captain")
print(my_bot.system)
