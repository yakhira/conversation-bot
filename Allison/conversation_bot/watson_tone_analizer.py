from watson_developer_cloud import ToneAnalyzerV3

class watson_tone_analizer:
    def __init__(self, username, password, version='2016-05-19'):
        self.username = username
        self.password = password
        self.version  = version 
    def watson_tone_analizer(self, text):
        tone = None

        toneanalizer = ToneAnalyzerV3(
            username = self.username,
            password = self.password,
            version  = self.version
        )

        response = toneanalizer.tone(
            text = text
        )

        for tone in response['document_tone']['tone_categories'][0]['tones']:
            if tone['score'] > 0.5:
               tone = tone['tone_name']

        return tone
