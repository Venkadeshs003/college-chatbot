import json
import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download('punkt')

class CollegeChatBot:
    def __init__(self, intents_file):
        with open(intents_file, 'r') as file:
            self.data = json.load(file)
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
        self.train_data()

    def train_data(self):
        patterns = []
        labels = []
        for intent in self.data['intents']:
            for pattern in intent['patterns']:
                patterns.append(pattern)
                labels.append(intent['tag'])
        X = self.vectorizer.fit_transform(patterns)
        self.model.fit(X, labels)

    def get_response(self, user_input):
        X_test = self.vectorizer.transform([user_input])
        predicted_tag = self.model.predict(X_test)[0]
        for intent in self.data['intents']:
            if intent['tag'] == predicted_tag:
                return random.choice(intent['responses'])
        return "Sorry, I didn’t understand that."

