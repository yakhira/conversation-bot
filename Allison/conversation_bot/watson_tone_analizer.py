from watson_developer_cloud import ToneAnalyzerV3

class watson_tone_analizer(object):
    """Tone analizer by IBM Watson"""
    def __init__(self, username, password, version="2016-05-19"):
        self.username = username
        self.password = password
        self.version = version
    def tone_analizer(self, text):
        """Send to IBM tone analizer service"""
        tone = None

        toneanalizer = ToneAnalyzerV3(
            username=self.username,
            password=self.password,
            version=self.version
        )

        response = toneanalizer.tone(
            text=text
        )

        for tone in response["document_tone"]["tone_categories"][0]["tones"]:
            if tone["score"] > 0.5:
                tone = tone["tone_name"]
        return tone
