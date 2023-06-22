import requests, random, tweepy
import keys

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


def post_tweet(api: tweepy.API, client:tweepy.Client, message):
    client.create_tweet(text=message)
    print('Posted tweet')


year = random.randrange(1994, 2022)

if year in [1994, 1996, 1998, 1999, 2003]:
    race = random.randrange(1, 16)
elif year in [1995, 1997, 2000, 2001, 2002, 2007, 2009, 2020]:
    race = random.randrange(1, 17)
elif year in [2004, 2006, 2008]:
    race = random.randrange(1, 18)
elif year in [2005, 2010, 2011, 2013, 2014, 2015]:
    race = random.randrange(1, 19)
elif year in [2012, 2017]:
    race = random.randrange(1, 20)
elif year in [2016, 2018, 2019]:
    race = random.randrange(1, 21)
else:
    race = random.randrange(1, 22)

url = f"http://ergast.com/api/f1/{year}/{race}/results.json"

# Request the data
request = requests.get(url)
content = request.json()

# Get the data
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

# Create the tweet.
message = "The " + circuit['raceName'] + " in the " + circuit['season'] + \
          " season took place on " + circuit['date'] + " at the " \
          + circuit_name["circuitName"] + ", the winning driver was " \
          + driver['givenName'] + " " + driver['familyName'] + \
          " - " + driver['code'] + " racing for " + constructor['name'] + ". "

# Post the tweet
if __name__ == '__main__':
    api = get_api()
    client = get_client()
    post_tweet(api, client, message)









