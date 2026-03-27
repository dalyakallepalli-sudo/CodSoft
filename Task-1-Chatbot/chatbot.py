import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
tokens = wordpunct_tokenize(text)

# Download datasets (only first time)
nltk.download('punkt')
nltk.download('stopwords')

knowledge_base = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What can I do for you?",
    "name": "I am an NLP-based chatbot.",
    "python": "Python is widely used in AI and Data Science.",
    "ai": "AI stands for Artificial Intelligence.",
    "internship": "Internships provide practical experience.",
    "bye": "Goodbye! Have a great day!"
}

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in string.punctuation]
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return tokens

def get_response(user_input):
    tokens = preprocess(user_input)

    for word in tokens:
        if word in knowledge_base:
            return knowledge_base[word]

    return "Sorry, I didn't understand that. Please try again."

def run_chatbot():
    print("🤖 NLP Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("🤖 Chatbot:", knowledge_base["bye"])
            break

        print("🤖 Chatbot:", get_response(user_input))

if __name__ == "__main__":
    run_chatbot()
