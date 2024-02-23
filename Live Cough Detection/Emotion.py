from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Define an empty string to hold the recognized text
text = ""

# Use microphone as audio source
with sr.Microphone() as source:
    print('Clearing background noise....')
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print('Waiting for your message....')
    recorded_audio = recognizer.listen(source)
    print('Done recording..')

try:
    print('Printing the message..') 
    # Recognize speech using Google Cloud Speech-to-Text API
    text = recognizer.recognize_google(recorded_audio, language='en-US')
    print('Your message: {}'.format(text))
except Exception as ex:
    print(ex)

# Sentiment analysis
analyser = SentimentIntensityAnalyzer()

# Split the recognized text into sentences
sentences = text.split('.') if text else []  # Split by period assuming sentences are separated by periods
for sentence in sentences:
    # Perform sentiment analysis on each sentence
    v = analyser.polarity_scores(sentence)
    print("Sentiment for '{}': {}".format(sentence, v))
