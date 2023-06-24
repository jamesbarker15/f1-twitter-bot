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


def post_tweet(api: tweepy.API, client: tweepy.Client, message):
    client.create_tweet(text=message)
    print('Posted tweet')


# Select a year between 1950 and 2022 at random
year = random.randrange(1950, 2022)

# Select a race number, dependent on how many races there were that year.
if year in [1950, 1955]:
    race = random.randrange(1, 7)
elif year in [1951, 1952, 1956, 1957, 1961]:
    race = random.randrange(1, 8)
elif year in [1953, 1954, 1959, 1962, 1966]:
    race = random.randrange(1, 9)
elif year in [1960, 1963, 1964, 1965]:
    race = random.randrange(1, 10)
elif year in [1958, 1967, 1969, 1971]:
    race = random.randrange(1, 11)
elif year in [1968, 1972]:
    race = random.randrange(1, 12)
elif year in [1970]:
    race = random.randrange(1, 13)
elif year in [1975, 1980]:
    race = random.randrange(1, 14)
elif year in [1973, 1974, 1979, 1981, 1983]:
    race = random.randrange(1, 15)
elif year in [1990, 1991, 1992, 1993, 1994, 1996, 1998, 1999, 2003]:
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

url = f"https://ergast.com/api/f1/{year}/{race}/results.json"

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

# Create the tweet, the using try and except for older data which doesn't
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








