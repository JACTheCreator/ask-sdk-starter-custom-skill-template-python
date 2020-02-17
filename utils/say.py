from constants.intents import (FIRST_ORDER_INTENT, SECOND_ORDER_INTENT,
                               THIRD_ORDER_INTENT)

class say(object):

    @staticmethod    
    def welcome():
        return """
            Welcome.
        """
    
    @staticmethod
    def firstorder():
        return """
            First intent called.
        """

    @staticmethod
    def secondorder():
        return """
            Second intent called.
        """

    @staticmethod
    def thirdorder():
        return """
            Third intent called.
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
		
        if set(intent) == set([FIRST_ORDER_INTENT]):
            return invalid_speech + """
            One or Uno. The First intent should be called here.
            """
        elif set(intent) == set([SECOND_ORDER_INTENT]):
            return invalid_speech + """
            Two or dos. The Second intent should be called here.
            """
        elif set(intent) == set([THIRD_ORDER_INTENT]):
            return invalid_speech + """
            Three or tres. The Third intent should be called here.
            """
        
        return invalid_speech