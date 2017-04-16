from watson_developer_cloud import TextToSpeechV1
from pyaudio import PyAudio

class watson_text_to_speech(object):
    """Text to speech recognition by IBM Watson"""
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.rate = 22050
        self.sampwidth = 2
        self.nchannels = 1
        self.chank = 2048
        self.accept = "audio/wav"
        self.voice = "en-US_AllisonVoice"
        self.response = None
    def text_to_speech(self, text):
        """Send to IBM text to speech recognition service"""
        texttospeech = TextToSpeechV1(
            username=self.username,
            password=self.password
        )

        response = texttospeech.synthesize(
            text=text,
            accept=self.accept,
            voice=self.voice
        )

        self.response = response
    def play_audio(self):
        """Play audio"""
        audio = PyAudio()
        stream = audio.open(format=audio.get_format_from_width(self.sampwidth),
                            channels=self.nchannels,
                            rate=self.rate,
                            output=True)
        stream.write(self.response)
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
