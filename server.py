from flask import Flask, render_template,request

from EmotionDetection.emotion_detection import emotion_detector

app=Flask("emotionDetector")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET'])
def emotionDetector():
    if request.method == 'GET':
        textToAnalyze=request.args.get('textToAnalyze')
    else:
        return {'method not allowed'}, 405

    if len(textToAnalyze) == 0:
        return "Please enter text to analyze"
    
    result=emotion_detector(textToAnalyze)
    
    formattedText=f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}."
    formattedText = formattedText + f"The dominant emotion is {result['dominant_emotion']}."
    
    return formattedText

if __name__ == "__main__":
    app.run(host='localhost', port=5000) 