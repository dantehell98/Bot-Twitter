import tweepy

def access():

    #tokens lecture
    f = open('./tokens.txt', 'r')
    #Have to eliminate the last caracter
    consumer_key = f.readline().replace("\n","")
    consumer_secret = f.readline().replace("\n","")
    access_token = f.readline().replace("\n","")
    access_token_secret = f.readline().replace("\n","")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api
