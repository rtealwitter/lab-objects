"""Exercise the student's classes together in a small feed.

Run from the lab-objects folder. Requirements and expected output are on the
course lab page linked in README.md. No class implementations are supplied here.
"""

from lab_classes import Tweet, User


class Announcement:
    def __init__(self, text):
        self.text = text


def show(post):
    print(post.text)


def rehearse_account():
    account = User('alice')
    print('account:', account)
    account.follow()
    account.follow()
    account.unfollow()
    print('followers after two follows and one unfollow:', account.followers)
    account.unfollow()
    account.unfollow()
    print('followers after extra unfollows:', account.followers)
    print('same account loaded again:', account == User('alice'))
    print('different account:', account == User('bob'))


def rehearse_posts():
    account = User('alice')
    post = Tweet(account.username, 'Game night! #python #games #python')
    other = Tweet('bob', 'I will bring a game.')
    print(post)
    post.like()
    post.like()
    post.unlike()
    print('likes after two likes and one unlike:', post.likes)
    post.unlike()
    post.unlike()
    print('likes after extra unlikes:', post.likes)
    print('hashtags:', post.hashtags())
    print("other tweet's likes:", other.likes)
    print("plain tweet's hashtags:", other.hashtags())


def rehearse_feed():
    print('feed text:')
    show(Tweet('alice', 'Game night! #python #games #python'))
    show(Announcement('Doors open at six.'))


def main():
    for name, rehearsal in [
        ('Account', rehearse_account),
        ('Posts', rehearse_posts),
        ('Feed', rehearse_feed),
    ]:
        try:
            rehearsal()
        except Exception as error:
            # Keep the other practice scenes available while methods are unfinished.
            print(f'{name} rehearsal stopped: {type(error).__name__}: {error}')
            print('Check the related methods with python3 -m doctest lab_classes.py.')


if __name__ == '__main__':
    main()
