"""Module for detecting emotions in text using Watson NLP API."""

import json
import requests


def emotion_detector(text_to_analyze):
    """Analyze emotions in the given text using Watson NLP.

    Args:
        text_to_analyze (str): The input text to analyze.

    Returns:
        dict: Emotion scores for anger, disgust, fear, joy, and sadness.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    if len(text_to_analyze) == 0:
        result = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None}
    else:
        response = requests.post(url, json=myobj, headers=headers, timeout=10)
        formatted_response = json.loads(response.text)
        result = formatted_response['emotionPredictions'][0]['emotion']

    print("result in emotion detection  : ", result)
    return result