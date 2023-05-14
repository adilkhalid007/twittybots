import tweepy
import requests
import json
import os
import openai
from datetime import datetime, timedelta
import pytz
import time

# Authenticate with the Twitter API
auth = tweepy.OAuth1UserHandler(
    os.environ['TWITTER_CONSUMER_KEY'],
    os.environ['TWITTER_CONSUMER_SECRET'],
    os.environ['TWITTER_ACCESS_TOKEN'],
    os.environ['TWITTER_ACCESS_TOKEN_SECRET']
)

# Create the API object
api = tweepy.API(auth)

# Authenticate with the OpenAI API
openai.api_key = os.environ['OPENAI_API_KEY']

# Define the timezone to use for scheduling tweets
timezone = pytz.timezone('US/Eastern')

# Define the maximum number of attempts to generate a quote
max_attempts = 5

# Define the prompt to use for generating quotes
prompt = "Generate a motivational quote"

# Define the OpenAI engine to use for generating quotes
engine = "text-davinci-002"

# Define a function to generate a quote using the OpenAI API
def generate_quote():
    attempts = 0
    while attempts < max_attempts:
        try:
            response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                max_tokens=64,
                n=1,
                stop=None,
                temperature=0.5,
            )
            quote = response.choices[0].text.strip()
            return quote
        except Exception as e:
            attempts += 1
            print(f"Error generating quote: {e}")
    return None

# Define a function to schedule a tweet with the given text at the given time
def schedule_tweet(text):
    # Get the current time
    now = datetime.now(timezone)

    # Round the current time up to the nearest half hour
    if now.minute < 30:
        scheduled_time = now.replace(minute=30, second=0, microsecond=0)
    else:
        scheduled_time = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)

    # Schedule the tweet
    api.update_status(text)
    print(f"Tweet scheduled for {scheduled_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# Define a function to run the bot
def run_bot():
    while True:
        # Generate a quote
        quote = generate_quote()
        if quote is None:
            continue

        # Schedule the tweet
        schedule_tweet(quote)

        # Sleep for 30 minutes
        time.sleep(1800)

# Run the bot
run_bot()
