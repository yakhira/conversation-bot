#!/usr/bin/env python

import sys
import signal

from conversation_bot import watson_conversation
from conversation_bot import watson_text_to_speech
from conversation_bot import watson_tone_analizer
from conversation_bot import watson_speech_to_text
from conversation_bot import sphinx_speech_to_text
from conversation_bot import wit_speech_to_text

from getopt import getopt, GetoptError

__author__ = "Ruslan Iakhin"

def get_input_type(argv):
    """Function to determine input type"""
    input_type = "text"

    if len(argv) <= 1:
        print("usage: %s --input <text|voice>" % argv[0])
        sys.exit(2)

    try:
        opts, args = getopt(argv[1:], "i:", "input=")

        for opt, arg in opts:
            if opt == "--input":
                input_type = arg
            else:
                print("usage: %s --input <text|voice>" % argv[0])
                sys.exit(2)

    except GetoptError as error:
        print(error)
        sys.exit(2)
    return input_type

def main(argv):
    """Entry point"""
    input_type = "text"
    in_text = ""
    out_text = ""
    response = ""

    SPEECHTOTEXT_IBM_USERNAME = ""
    SPEECHTOTEXT_IBM_PASSWORD = ""

    CONVERSATION_IBM_USERNAME = ""
    CONVERSATION_IBM_PASSWORD = ""
    CONVERSATION_IBM_WORKSPACE = ""

    TEXTTOSPEECH_IBM_USERNAME = ""
    TEXTTOSPEECH_IBM_PASSWORD = ""

    TONEANALIZER_IBM_USERNAME = ""
    TONEANALIZER_IBM_PASSWORD = ""

    WIT_ACCESS_TOKEN = ""

    input_type = get_input_type(argv)

    conversation = watson_conversation(
        CONVERSATION_IBM_USERNAME, CONVERSATION_IBM_PASSWORD, CONVERSATION_IBM_WORKSPACE)
    toneanalizer = watson_tone_analizer(TONEANALIZER_IBM_USERNAME, TONEANALIZER_IBM_PASSWORD)
    texttospeech = watson_text_to_speech(TEXTTOSPEECH_IBM_USERNAME, TEXTTOSPEECH_IBM_PASSWORD)
    #speechtotext = watson_speech_to_text(SPEECHTOTEXT_IBM_USERNAME, SPEECHTOTEXT_IBM_PASSWORD)
    #speechtotext = wit_speech_to_text(WIT_ACCESS_TOKEN)
    speechtotext = sphinx_speech_to_text()

    response = conversation.send_message(in_text)
    texttospeech.text_to_speech(response)
    #texttospeech.play_audio()

    print("Watson: {0}".format(response))

    while True:
        if input_type == "voice":
            speechtotext.listen_from_michrophone()
            in_text = speechtotext.speech_to_text()
        else:
            if sys.version_info < (3, 0):
                in_text = raw_input("You: ")
            else:
                in_text = input("You: ")

        if in_text != "":
            print("You: {0}".format(in_text))

            conversation.set_context("tone", toneanalizer.tone_analizer(in_text))
            response = conversation.send_message(in_text)
            texttospeech.text_to_speech(response)
            texttospeech.play_audio()

            print("Watson: {0}".format(response))
        if "bye" in in_text:
            sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))
    main(sys.argv)
