from chatterbot import ChatBot
from chatterbot.trainers import CorpusTrainer
from nltk.chat.util import Chat, reflections
from nltk.corpus import nps_chat


from chatterbot import ChatBot
from nltk.chat.util import Chat, reflections
from nltk.corpus import nps_chat


chatbot = ChatBot('My ChatBot')


trainer = CorpusTrainer(chatbot)


trainer.train('nltk.corpus.nps_chat.english.greetings', 'nltk.corpus.nps_chat.english.question', 'nltk.corpus.nps_chat.english.conversations')


class ChatBotChat(Chat):
    def __init__(self, chatbot):
        self.chatbot = chatbot

    def respond(self, message):
        response = self.chatbot.get_response(message.text)
        return response.text


chat = ChatBotChat(chatbot)


chat.converse()
