from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk
from data import training_data
nltk.download('punkt_tab', quiet=True)

Hamza_assistant = ChatBot("Hamza_chatbot", logic_adapters=[
    {
    "import_path":"chatterbot.logic.BestMatch",
    "default_response":"Sorry I'm unable to respond yet",
    "maximum_similarity_threshold": 0.95
    }
                     ])

ListTrainer(Hamza_assistant).train(training_data)

while True:
    user_input = input("User: ")
    print("Chatbot: "+str(Hamza_assistant.get_response(user_input)))