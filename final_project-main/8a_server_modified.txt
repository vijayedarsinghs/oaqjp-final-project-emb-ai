"""Flask server for the Emotion Detection web application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def sent_detector():
    """Analyze emotion from query param and return a formatted result."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['anger'] is None:
        ret_data = "Invalid text! Please try again!"
    else:
        ret_data = f"The given text has been identified as {response}"

    print("server response", ret_data)
    return ret_data


@app.route("/")
def render_index_page():
    """Render the main index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
    