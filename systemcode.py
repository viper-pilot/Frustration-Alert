from transformers import pipeline

# Initialize a pre-trained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Function to check if a message is frustrated
def is_frustrated(message):
    sentiment = sentiment_analyzer(message)[0]
    label = sentiment['label']
    score = sentiment['score']
    
    # If the sentiment is negative and the score is high, it's likely frustration
    if label == "NEGATIVE" and score > 0.75:
        return True
    return False

# User Input
message = input("Enter your message: ")

# Check for frustration
if is_frustrated(message):
    print("The message indicates frustration.")
else:
    print("The message does not indicate frustration.")
