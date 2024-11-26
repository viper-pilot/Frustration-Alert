from transformers import pipeline

# Initialize a pre-trained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Function to check for different emotional states
def check_emotion(message):
    sentiment = sentiment_analyzer(message)[0]
    label = sentiment['label']
    score = sentiment['score']
    
    emotions = []

    # Check if the sentiment is negative and score is high
    if label == "NEGATIVE":
        if score > 0.75:
            emotions.append("Frustration")
        elif 0.5 < score <= 0.75:
            emotions.append("Sadness")
        elif score <= 0.5:
            emotions.append("Guilt or Grievance")
    
    # Check if the sentiment is positive
    if label == "POSITIVE":
        if score > 0.75:
            emotions.append("Happiness")
        elif 0.5 < score <= 0.75:
            emotions.append("Excitement")
    
    return emotions

# User Input
message = input("Enter your message: ")

# Check for emotions
emotions = check_emotion(message)

if emotions:
    print(f"The message indicates the following emotions: {', '.join(emotions)}")
else:
    print("The message does not indicate any specific emotions.")
