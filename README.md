Twittybot is a python program which uses tweepy and OpenAi to generate tweets by it's own and then post them on twitter.

Dependencies:

Install the following packages using pip.  (pip install tweepy) & (pip install openai)

CONFIGURATION: 

Download the file named twitter-bot.py from the repo.
Then create your twitter developer account, and ask twitter for Elevated access by filling up the application they will provide, wait for like 48 hours for the application to get approved (mine took few minutes) and then create your app on twitter.

After you create your app, you should see teh api keys and secret key. Copy them and replace them on line 12 of twittybots.py: 
api_key  ="YOUR API KEY FROM TWITTER"
and do the same for line 13 and replace it with the api key secret and then get generate access token and secret on twitter developer platform.

Now that we have the twitter ready, let's do the OpenAi, go to openai official website and generate an api key for yourself and then replace it on the line 22: 
openai.api_key = "OPEN AI KEY"

It defines a new schedule_tweet function that rounds the current time up to the nearest half hour and schedules a tweet for that time. The run_bot function generates a quote, schedules a tweet for the next half hour, and sleeps for 30 minutes before repeating the process. To stop the bot, you can simply terminate the Python process running the script.
This code authenticates with the Twitter API and the OpenAI API, defines a function to generate a motivational quote using AI, and defines a function to schedule a tweet with the given text at the given time. The run_bot function generates a quote, schedules a tweet for the next day at the specified time, and prints a message to the console indicating when the tweet is scheduled for.
