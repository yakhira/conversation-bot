import speech_recognition
import requests

class watson_speach_to_text:
    def __init__(self, username, password):
         self.speachrecognition = speech_recognition.Recognizer()
         self.username = username
         self.password = password
    def set_audio_from_url(self, audio_url):
        self.audio = requests.get(audio_url) 
    def listen_from_michrophone(self):
        with speech_recognition.Microphone() as source:
            self.audio = self.speachrecognition.listen(source)
    def watson_speach_to_text_service(self):
        text = ''
        try:
            text = self.speachrecognition.recognize_ibm(self.audio, username=self.username, password=self.password)
        except speech_recognition.UnknownValueError:
            text = ''
        except speech_recognition.RequestError as error:
            text = ''
        return text
    
