from textblob import TextBlob
import random

def detect_sentiment(text):
    """Detect the sentiment of the user input using TextBlob with dynamic messages."""
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    # Dynamic negative messages
    negative_messages = [
        "I’m sorry to hear you might be feeling down. Let’s address your concerns.",
        "It sounds tough—let’s work together to help you feel better.",
        "I’m here for you—let’s tackle this concern step by step.",
    ]
    
    # Dynamic positive messages
    positive_messages = [
        "I’m glad you’re feeling positive! Let’s address your query.",
        "Great to hear your good spirits—let’s handle your question now.",
        "Wonderful to see your positivity—let’s move forward with your query!",
    ]
    
    if sentiment < -0.1:
        return "negative", random.choice(negative_messages)
    elif sentiment > 0.1:
        return "positive", random.choice(positive_messages)
    return "neutral", ""