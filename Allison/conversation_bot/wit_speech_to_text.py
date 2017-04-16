import speech_recognition
import requests

class wit_speech_to_text(object):
    """Class to transcribe speech by wit.ai"""
    def __init__(self, access_token):
        self.speechrecognition = speech_recognition.Recognizer()
        self.audio = None
        self.access_token = access_token
    def listen_from_michrophone(self):
        """List from microphone"""
        with speech_recognition.Microphone() as source:
            self.audio = self.speechrecognition.listen(source)
    def speech_to_text(self):
        """Recognize audio stream"""
        text = ""

        try:
            text = self.speechrecognition.recognize_wit(self.audio, key=self.access_token)
        except speech_recognition.UnknownValueError:
            text = ""
        except speech_recognition.RequestError:
            text = ""
        return text
