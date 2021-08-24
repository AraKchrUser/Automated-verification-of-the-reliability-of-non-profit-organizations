from deeppavlov import configs, build_model
from collections import Counter


class Sentimental:
    def __init__(self, model):
        self.model = model
        # self.model = build_model(configs.classifiers.rusentiment_elmo_twitter_cnn, download=download)

    def sentimental_get(self, text):
        return self.model([text])

    def sentimental_feedback_prob(self, texts):
        feedback_list = list()
        for text in texts.split('.'):
            feedback = self.model([text])[0]
            if feedback == 'negative' or feedback == 'positive':
                print(text, feedback)
            feedback_list.append(feedback)
        return Counter(feedback_list)
