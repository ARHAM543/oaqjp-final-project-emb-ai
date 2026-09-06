import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response["emotionPredictions"][0]["emotion"]["joy"],
                         max(response["emotionPredictions"][0]["emotion"].values()))

    def test_anger(self):
        response = emotion_detector("I am really mad about this")
        self.assertEqual(response["emotionPredictions"][0]["emotion"]["anger"],
                         max(response["emotionPredictions"][0]["emotion"].values()))

    def test_disgust(self):
        response = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response["emotionPredictions"][0]["emotion"]["disgust"],
                         max(response["emotionPredictions"][0]["emotion"].values()))

    def test_sadness(self):
        response = emotion_detector("I am so sad about this")
        self.assertEqual(response["emotionPredictions"][0]["emotion"]["sadness"],
                         max(response["emotionPredictions"][0]["emotion"].values()))

    def test_fear(self):
        response = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response["emotionPredictions"][0]["emotion"]["fear"],
                         max(response["emotionPredictions"][0]["emotion"].values()))

if __name__ == '__main__':
    unittest.main()
