import tweepy
import access


def bot():
    api = access.access()
    user = api.me()
    for friend in user.friends():
        print(friend.screen_name)


if __name__ == "__main__":
    bot()
