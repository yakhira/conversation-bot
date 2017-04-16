from watson_developer_cloud import ConversationV1

class watson_conversation(object):
    """Conversation service by IBM Watson"""
    def __init__(self, username, password, workspace, version="2017-02-03"):
        self.username = username
        self.password = password
        self.version = version
        self.context = {}
        self.workspace = workspace
    def set_context(self, name, value):
        """Get context"""
        self.context[name] = value
    def get_context(self, name):
        """Set context"""
        if name in self.context:
            return self.context[name]
        return None
    def send_message(self, text):
        """Send to conversation services by IBM Watson"""
        response = ""

        conversation = ConversationV1(
            username=self.username,
            password=self.password,
            version=self.version
        )

        conversation_response = conversation.message(
            workspace_id=self.workspace,
            message_input={"text":text},
            context=self.context
        )
        self.context = conversation_response["context"]

        if len(conversation_response["output"]["text"]) > 0:
            for output_text in conversation_response["output"]["text"]:
                if len(output_text) > 0:
                    response += output_text + " "
        else:
            response = "I didn`t understand you."

        return response
