import sys
import signal

from conversation_bot import watson_conversation
from conversation_bot import watson_speach_to_text
from conversation_bot import watson_text_to_speach
from conversation_bot import watson_tone_analizer

from getopt import getopt,GetoptError

__author__ = 'Ruslan Iakhin'

def get_input_type(argv):
    input_type = 'text'

    if len(argv) <= 1:
        print("usage: %s --input <text|voice>" % argv[0])
        sys.exit(2)

    try:
        opts, args = getopt(argv[1:],"i:","input=")
        
        for opt, arg in opts:
            if opt == '--input':
                input_type = arg
            else:
                print("usage: %s --input <text|voice>" % argv[0])
                sys.exit(2)

    except GetoptError as error:
        print(error)
        sys.exit(2)
    return input_type

def main(argv):
    input_type = 'text'
    in_text    = ''
    out_text   = ''
    response   = ''

    SPEECHTOTEXT_IBM_USERNAME = ''
    SPEECHTOTEXT_IBM_PASSWORD = ''

    CONVERSATION_IBM_USERNAME = ''
    CONVERSATION_IBM_PASSWORD = ''
    CONVERSATION_IBM_WORKSPACE= ''

    TEXTTOSPEECH_IBM_USERNAME = ''
    TEXTTOSPEECH_IBM_PASSWORD = ''

    TONEANALIZER_IBM_USERNAME = ''
    TONEANALIZER_IBM_PASSWORD = ''

    input_type = get_input_type(argv)
    
    conversation = watson_conversation(CONVERSATION_IBM_USERNAME, CONVERSATION_IBM_PASSWORD, CONVERSATION_IBM_WORKSPACE)
    toneanalizer = watson_tone_analizer(TONEANALIZER_IBM_USERNAME, TONEANALIZER_IBM_PASSWORD)
    texttospeach = watson_text_to_speach(TEXTTOSPEECH_IBM_USERNAME, TEXTTOSPEECH_IBM_PASSWORD)
    speachtotext = watson_speach_to_text(SPEECHTOTEXT_IBM_USERNAME, SPEECHTOTEXT_IBM_PASSWORD)

    response = conversation.watson_conversation_service(in_text)
    texttospeach.watson_text_to_speach_service(response)
    texttospeach.play_audio()

    print('Watson: %s' % response)

    while True:
        if input_type == 'voice':
            speachtotext.listen_from_michrophone()
            in_text = speachtotext.watson_speach_to_text_service()

            print('You: %s' % in_text)
        else:
            if sys.version_info < (3,0):
                in_text = raw_input("You: ")
            else:
                in_text = input("You: ")

        if in_text == '':
            print('You: <not recognized, say again>')
        else:
            conversation.set_context('tone', toneanalizer.watson_tone_analizer(in_text))
            response = conversation.watson_conversation_service(in_text)
            texttospeach.watson_text_to_speach_service(response)
            texttospeach.play_audio()      

            print('Watson: %s' % response)
        if 'bye' in in_text:
            sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))
    main(sys.argv)
