# Slack Chatbot with Llama Index

This is a Slack chatbot that utilizes the Llama Index library to provide document indexing and querying capabilities. The chatbot listens to incoming messages in a Slack workspace and performs queries on the indexed documents using Llama Index. It responds with the matching results from the index.

# Prerequisites

Before running the chatbot, make sure you have the following:

- Python 3.7 or higher installed
- Slack API credentials (bot token and signing secret)
- Environment variables configured in a `.env` file
- Document files to be indexed placed in a `data` folder in the project directory

# Configure environment variables:

Create a .env file in the project directory and add the following variables:
- SLACK_BOT_TOKEN=<your_slack_bot_token>
- SLACK_SIGNING_SECRET=<your_slack_signing_secret>
- SLACK_APP_TOKEN=<your_slack_app_token>
