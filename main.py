import requests
import random
import tweepy
import keys
import sqlite3

#Testing the pipeline.

# Functions
def get_api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    return tweepy.API(auth)


def get_client():
    client = tweepy.Client(consumer_key=keys.api_key,
                           consumer_secret=keys.api_secret,
                           access_token=keys.access_token,
                           access_token_secret=keys.access_token_secret,
                           bearer_token=keys.bearer_token)
    return client


def post_tweet(api: tweepy.API, client: tweepy.Client, message):
    client.create_tweet(text=message)
    print('Posted tweet')


# Pick a year at random between 1950 and 2022
year = random.randrange(1950, 2022)

# Connect to the database, select row with the year.
connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("SELECT races FROM f1_years WHERE year=?", (year, ))

# Return the number of races in that year from the database
data = cursor.fetchone()
races = data[0]

# Pick a random race between 1 and max number of races obtained from database
race = random.randrange(1, races)

# Formulate the API URL
url = f"https://ergast.com/api/f1/{year}/{race}/results.json"

# Request and get the data
request = requests.get(url)
content = request.json()

# Filter the data
data = content["MRData"]
race_table = data['RaceTable']
races = race_table["Races"]

# Access the race name, season and date
circuit = races[0]
circuit_name = circuit['Circuit']

# Access the winning driver and constructor
results = circuit["Results"]
winner = results[0]
driver = winner["Driver"]
constructor = winner["Constructor"]

# Create the tweet, using try and except for older data which doesn't
# contain driver codes
try:
    message = "The " + circuit['raceName'] + " in the " + circuit['season'] + \
              " season took place on " + circuit['date'] + " at the " \
              + circuit_name["circuitName"] + ", the winning driver was " \
              + driver['givenName'] + " " + driver['familyName'] + \
              " - " + driver['code'] + " racing for " + constructor[
                  'name'] + ". "
except:
    message = "The " + circuit['raceName'] + " in the " + circuit['season'] + \
              " season took place on " + circuit['date'] + " at the " \
              + circuit_name["circuitName"] + ", the winning driver was " \
              + driver['givenName'] + " " + driver['familyName'] + \
              " racing for " + constructor[
                  'name'] + ". "


# Post the tweet
if __name__ == '__main__':
    api = get_api()
    client = get_client()
    post_tweet(api, client, message)








