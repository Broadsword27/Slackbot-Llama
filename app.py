#Libary Modules needed for this script: slack_bolt, os, json, llama_index, openai
import os
import json
from dotenv import find_dotenv, load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from llama_index import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]

# Initialize the Slack app
app = App(token=SLACK_BOT_TOKEN)

# Load you data into 'Documents' a custom type by LlamaIndex
documents = SimpleDirectoryReader('./data').load_data() # Create a folder "data" and add your own KB

# Create an index of your documents
index = GPTVectorStoreIndex.from_documents(documents)

# Test the index with a query and print the result
# print(index.query('Who are the main approvers for contractor expenses?'))

# Listens to any incoming messages
@app.message("")
def message_all(message, say):
    # Print the incoming message text
    print(message['text'])
    
    # Query the index with the message text and get a response
    text = message['text']
    query_engine = index.as_query_engine()
    response = query_engine.query(text)
    
    # Extract the desired message and sources from the response object
    message = str(response)  # Convert the 'Response' object to a string
    sources = json.dumps(response.get_formatted_sources(length=100))
    
    # Print the message and sources and send them as a message back to the user
    print(message)
    print(sources)
    say(message + '\n\n' + sources)

@app.event("app_mention")
def handle_app_mention_events(body, say, logger):
    message = body["event"]
    text = message["text"]
    query_engine = index.as_query_engine()
    response = query_engine.query(text)
    message = str(response)
    say(message)

# Start the Socket Mode handler
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()