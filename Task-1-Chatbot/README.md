 ## Simple NLP Chatbot

This is a basic chatbot I built using Python and NLTK as part of my internship task.

The idea was to understand how chatbots work using simple NLP techniques instead of hardcoding only if-else conditions.

---

What it does

* Takes user input from the console
* Breaks the sentence into words (tokenization)
* Removes common words (like "is", "the", etc.)
* Checks for keywords and gives a response

---

 How to run

1. Install requirements:

```
pip install nltk
```

2. Run the file:

```
python chatbot.py
```

---

 Example

You: hi
Bot: Hello! What can I do for you?

You: what is ai
Bot: AI stands for Artificial Intelligence.

---

 What I learned

While doing this task, I understood:

* Basic NLP preprocessing
* How chatbots identify intent using keywords
* How to structure a simple Python project

---

 Future improvements

* Add more responses
* Make it work with a GUI
* Improve accuracy using better matching techniques
