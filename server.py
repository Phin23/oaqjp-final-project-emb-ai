"""
Flask server for Emotion Detection Application
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main application page"""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Endpoint for emotion detection
    Gets text from query parameter and returns formatted emotion analysis
    """
    # Get the text to analyze from request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)
    
    # Check if the response is valid
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    # Format the output as requested
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
    return formatted_response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
