from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name

from constants.intents import SECOND_ORDER_INTENT, THIRD_ORDER_INTENT

from utils.say import say

from utils.common import (set_next_intent, is_next_intent_error, 
                          handle_next_intent_error, set_prev_msg,
                          get_prev_msg)

class FirstOrderIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name(SECOND_ORDER_INTENT)(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Checking if this intent should play now.
        current_intent = [SECOND_ORDER_INTENT]
        if is_next_intent_error(handler_input = handler_input, current_intent = current_intent):
            return handle_next_intent_error(handler_input = handler_input)   

        # Setting the next intent.
        set_next_intent(handler_input = handler_input, 
                        next_intent = [THIRD_ORDER_INTENT])

        speech_text = say.firstorder()
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response