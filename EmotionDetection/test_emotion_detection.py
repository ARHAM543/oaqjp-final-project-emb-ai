from EmotionDetection import emotion_detector

def test_emotion_detector():
    assert emotion_detector("I am glad this happened")["emotionPredictions"][0]["emotion"]["joy"] == max(
        emotion_detector("I am glad this happened")["emotionPredictions"][0]["emotion"].values()
    )

    assert emotion_detector("I am really mad about this")["emotionPredictions"][0]["emotion"]["anger"] == max(
        emotion_detector("I am really mad about this")["emotionPredictions"][0]["emotion"].values()
    )

    assert emotion_detector("I feel disgusted just hearing about this")["emotionPredictions"][0]["emotion"]["disgust"] == max(
        emotion_detector("I feel disgusted just hearing about this")["emotionPredictions"][0]["emotion"].values()
    )

    assert emotion_detector("I am so sad about this")["emotionPredictions"][0]["emotion"]["sadness"] == max(
        emotion_detector("I am so sad about this")["emotionPredictions"][0]["emotion"].values()
    )

    assert emotion_detector("I am really afraid that this will happen")["emotionPredictions"][0]["emotion"]["fear"] == max(
        emotion_detector("I am really afraid that this will happen")["emotionPredictions"][0]["emotion"].values()
    )
