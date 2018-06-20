import tweepy
import validation


class bot():

    #API validation extracting tokens
    def __init__(self):
        self.api = access.access()

    #Extract every friend of the app's owner
    def getMyFriends(self):
        user = self.api.me()
        for friend in user.friends():
            print(friend.screen_name)


def main():
    mybot = bot()
    mybot.getMyFriends()

if __name__ == "__main__":
    main()
