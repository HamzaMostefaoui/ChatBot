from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk

nltk.download('punkt_tab')

my_chatbot = ChatBot("Chatbot", logic_adapters=["chatterbot.logic.BestMatch"])

def bot_training(bot:ChatBot,training_data:list):
    ListTrainer(bot).train(training_data)

def get_response(bot:ChatBot):
    user_input = input("User: ")
    return bot.get_response(user_input)

training_list = [
                "hi",
                "hi there",
                "what's your name",
                "I'm a chatbot",
                "how old are you ?",
                "I'm ageless!"

]

list_trainer = ListTrainer(bot)

list_trainer.train(training_list)

user_response = input("User: ")

print(bot.get_response(user_response))