import json
import os
from src.services.unknown_questions_service import UnkownQuestionsService


CURRENT_DIR, _ = os.path.split(os.path.abspath(__file__))


class FatequinoChatbot():
    def __init__(self, bot, Trainer):
        self.bot = bot
        self.trainer = Trainer(self.bot)
        self.unknown_questions = UnkownQuestionsService()
        self.conversations = json.loads(open(os.path.join(CURRENT_DIR, 'trainn/conversas.json'), 'r').read())

    def trainn_bot(self, talk):
        return self.trainer.train(talk)

    def sent_message(self, received_message):
        processedAnswer = self.bot.get_response(received_message)
        print("Received a message '{}'. Achieved a confidence of {} for the answer '{}'"
              .format(received_message, processedAnswer.confidence, str(processedAnswer)))

        if (float(processedAnswer.confidence) >= 0.5):
            return str(processedAnswer)
        if received_message in self.conversations:
            return str(self.bot.get_response(received_message))
        else:
            if not (received_message in self.conversations):
                self.unknown_questions.create(received_message)
                return "Ainda não sei te responder sobre isso, mas irei pesquisar para conseguir te responder."
