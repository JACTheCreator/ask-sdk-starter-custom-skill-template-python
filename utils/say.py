
class say(object):

    @staticmethod    
    def welcome():
        return """
            Welcome.
        """
    
    @staticmethod
    def didnothear():
        return """
            I did not get that. 
        """

    @staticmethod
    def help(prev_msg):
        return """
            Help.
        """ + prev_msg

    @staticmethod
    def bye():
        return """
            GoodBye.
        """

    @staticmethod
    def exceptionerror():
        return """
            Sorry, there was some problem. Please try again Later!!
		"""
    
    @staticmethod
    def next_intent_error_handle(intent, handler_input):
        invalid_speech = 'Silly! That is not right! I was expecting you to tell me'
		
        # if set(intent) == set([GET_GUESS_MY_NUMBER_INTENT, GET_GUESS_ALEXA_NUMBER_INTENT]):
        #     return invalid_speech + """
        #     the game mode. Just say guess your number 
        #     if you want to guess my number, or, say guess my secret number 
        #     if you want me to guess your secret number.
        #     """
        return invalid_speech