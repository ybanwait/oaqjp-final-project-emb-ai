"""
This module contains function to analyze the text and detect emotion from text. 
"""
#import the required packages, methods
from flask import Flask, render_template,request

from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route("/")
def index():
    """
    Set up the default page.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET'])
def analyze_emotions():
    """
    function to analyze text entered by user
    """
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    #If dominant emotion is None then we send error message
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # send back formatted output
    formatted_text = "For the given statement, the system response "
    formatted_text += f"is 'anger': {result['anger']}, 'disgust': {result['disgust']}"
    formatted_text += f", 'fear': {result['fear']}, 'joy': {result['joy']}"
    formatted_text += f", 'sadness': {result['sadness']}."
    formatted_text += f" The dominant emotion is {result['dominant_emotion']}."
    return formatted_text

# Finally run the app at port 5000.
if __name__ == "__main__":
    app.run(host='localhost', port=5000)
