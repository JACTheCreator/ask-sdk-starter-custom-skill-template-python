import os
from dotenv import load_dotenv
from flask import Flask
from flask_ask_sdk.skill_adapter import SkillAdapter
from ask_sdk_core.skill_builder import SkillBuilder

from intents.launch_request_handler import LaunchRequestHandler
from intents.help_intent_handler import HelpIntentHandler
from intents.cancel_or_stop_intent_handler import CancelOrStopIntentHandler
from intents.session_ended_request_handler import SessionEndedRequestHandler
from intents.catch_all_exception_handler import CatchAllExceptionHandler

load_dotenv()

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(HelpIntentHandler())

sb.add_exception_handler(CatchAllExceptionHandler())


app = Flask(__name__)
skill_response = SkillAdapter(skill = sb.create(), 
                              skill_id = os.getenv('SKILL_ID'), 
                              app = app)

skill_response.register(app = app, route = "/")

if __name__ == '__main__':
    app.run(threaded = True)
