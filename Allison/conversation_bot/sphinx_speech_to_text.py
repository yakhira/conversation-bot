import speech_recognition
import requests

class sphinx_speech_to_text(object):
    """Class to transcribe speech by sphinx"""
    def __init__(self):
        self.speechrecognition = speech_recognition.Recognizer()
        self.audio = None
    def listen_from_michrophone(self):
        """List from microphone"""
        with speech_recognition.Microphone() as source:
            self.audio = self.speechrecognition.listen(source)
    def speech_to_text(self):
        """Recognize audio stream"""
        text = ""

        try:
            text = self.speechrecognition.recognize_sphinx(self.audio)
        except speech_recognition.UnknownValueError:
            text = ""
        except speech_recognition.RequestError:
            text = ""
        return text
