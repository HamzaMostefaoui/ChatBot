import nltk
nltk.download("punkt_tab", quiet=True)
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request
from data import training_data


bot = ChatBot(
    "bot",
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "default_response": "Sorry I'm unable to respond please check this link for more info: www.linkedin.com/in/hamza-mostefaoui",
            "maximum_similarity_threshold": 0.90,
        }
    ],
)

ListTrainer(bot).train(training_data)


app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

# while True:
#     user_input = input("User: ")
#     print("Chatbot: " + str(bot.get_response(user_input)))

@app.route("/get")
def get_chatbot_response():
   user_text =  request.args.get('userMessage')
   return str(bot.get_response(user_text))


if __name__ == "__main__":
    app.run(debug=True)
