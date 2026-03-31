from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result1 = emotion_detector("I am glad this happened")
        key = max(result1, key=result1.get)
        print(f"Detected emotion: {key}")
        self.assertEqual(key,"joy")

        result1 = emotion_detector("I am really mad about this")
        key = max(result1, key=result1.get)
        print(f"Detected emotion: {key}")
        self.assertEqual(key,"anger")

        result1 = emotion_detector("I feel disgusted just hearing about this")
        key = max(result1, key=result1.get)
        print(f"Detected emotion: {key}")
        self.assertEqual(key,"disgust")

        result1 = emotion_detector("I am so sad about this")
        key = max(result1, key=result1.get)
        print(f"Detected emotion: {key}")
        self.assertEqual(key,"sadness")

        result1 = emotion_detector("I am really afraid that this will happen")
        key = max(result1, key=result1.get)
        print(f"Detected emotion: {key}")
        self.assertEqual(key,"fear")

unittest.main()