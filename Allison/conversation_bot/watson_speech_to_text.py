import speech_recognition
import requests

class watson_speech_to_text(object):
    """speech to text recognition by IBM Watson"""
    def __init__(self, username, password):
        self.speechrecognition = speech_recognition.Recognizer()
        self.username = username
        self.password = password
        self.audio = None
    def set_audio_from_url(self, audio_url):
        """Set audio stream"""
        self.audio = requests.get(audio_url)
    def listen_from_michrophone(self):
        """List from microphone"""
        with speech_recognition.Microphone() as source:
            self.audio = self.speechrecognition.listen(source)
    def speech_to_text(self):
        """Send to IBM speech recognition service"""
        text = ""
        try:
            text = self.speechrecognition.recognize_ibm(
                self.audio, username=self.username, password=self.password)
        except speech_recognition.UnknownValueError:
            text = ""
        except speech_recognition.RequestError:
            text = ""
        return text

