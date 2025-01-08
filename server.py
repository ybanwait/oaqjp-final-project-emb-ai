#import the required packages, methods
from flask import Flask, render_template,request

from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

# Set up the default page.
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET'])
def emotionDetector():
    #function to analyze text entered by user
    textToAnalyze = request.args.get('textToAnalyze')
    result = emotion_detector(textToAnalyze)
    #If dominant emotion is None then we send error message
    if result['dominant_emotion'] == None:
        return "Invalid text! Please try again!"

    # send back formatted output
    formattedText = f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}."
    formattedText = formattedText + f"The dominant emotion is {result['dominant_emotion']}."
    
    return formattedText

# Finally run the app at port 5000.
if __name__ == "__main__":
    app.run(host='localhost', port=5000) 