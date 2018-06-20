import tweepy

def access():
    f = open('./tokens.txt', 'r')
    consumer_key = f.readline().replace("\n","")
    consumer_secret = f.readline().replace("\n","")
    access_token = f.readline().replace("\n","")
    access_token_secret = f.readline().replace("\n","")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    user = api.me()
    print(user.name)

access()
