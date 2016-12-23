import praw
import pdb
import re
import os
import time

reddit = praw.Reddit(client_id='', #Program will not compile without filled in information
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')

def comment_post(comment_search, comment_reply):
    print(comment_search)
    print(comment_reply)
    if re.search(comment_search, comment.body, re.IGNORECASE):

        print('Bot replying to:', comment.id)
        print('Bot saying:', comment_reply)
        comment.reply(comment_reply)
        time.sleep(5)
        posts_replied_to.append(comment.id)
        print(posts_replied_to)

posts_replied_to = []

if not os.path.isfile('posts_replied_to.txt'):
    print('creating a file')
    text_file = open('posts_replied_to.txt', 'w')
    text_file.close()

else:
    with open('posts_replied_to.txt', 'r') as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split('\n')
        posts_replied_to = list(filter(None, posts_replied_to))

subreddit = reddit.subreddit('me_irlbot')
for comment in subreddit.stream.comments():
    if comment.id not in posts_replied_to:
        print('new comment in stream: ',comment.id)
        comment_post('REPLACE HERE', 'REPLACE HERE')
        comment_post('REPLACE HERE', 'REPLACE HERE')

    with open('posts_replied_to.txt', 'w') as f:
        for comment_id in posts_replied_to:
            f.write(comment_id + '\n')
        f.close()

