# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer

# # Download the VADER lexicon if not already downloaded
# nltk.download('vader_lexicon')

# def detect_emotion(text):
#     analyzer = SentimentIntensityAnalyzer()
#     sentiment_scores = analyzer.polarity_scores(text)

#     if sentiment_scores['compound'] >= 0.05:
#         return 'Positive'
#     elif sentiment_scores['compound'] <= -0.05:
#         return 'Negative'
#     else:
#         return 'Neutral'

# # Example usage with your provided responses
# responses = {
#     'How are you feeling right now?': 'hii',
#     'Can you describe your mood?': 'hello',
#     'What thoughts are on your mind?': 'ggg',
#     'How was your day?': 'ggg',
#     'How do you feel about this question?': 'bbb'
# }

# for question, answer in responses.items():
#     emotion = detect_emotion(answer)
#     print(f"{question}: {emotion} emotion")



import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download the VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

def detect_emotion(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Example usage with your provided responses
responses = {
    'How are you feeling right now?': 'not good',
    'Can you describe your mood?': 'iam not ok',
    'What thoughts are on your mind?': 'my mind is blank',
    'How was your day?': 'not going good',
    'How do you feel about this question?': 'ok'
}

# Collect emotions from responses
emotions = [detect_emotion(answer) for answer in responses.values()]

# Calculate emotion counts
emotion_counts = {'Positive': emotions.count('Positive'), 'Negative': emotions.count('Negative'), 'Neutral': emotions.count('Neutral')}

# Calculate average emotion
total_emotions = len(emotions)

if total_emotions > 0:
    # Find the emotion with the maximum count
    average_emotion = max(emotion_counts, key=emotion_counts.get)
    print(f"Average Emotion: {average_emotion} ({emotion_counts['Positive']} positive, {emotion_counts['Negative']} negative, {emotion_counts['Neutral']} neutral)")

    # Additional conditions based on sentiment scores
    if emotion_counts['Negative'] > total_emotions * 0.5:
        print("You might be experiencing elevated stress levels. Consider talking to someone or engaging in activities that help you relax.")
    elif emotion_counts['Neutral'] > total_emotions * 0.5:
        print("Your responses seem neutral. It's essential to check in on yourself and address any sources of stress or concern.")
    else:
        print("Your responses indicate a generally positive sentiment. Keep up the positive outlook!")

else:
    print("No responses to analyze.")
