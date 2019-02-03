import praw
r=praw.Reddit('bot1')

user = r.redditor('arpan8')

target_subreddit = 'PythonForEngineers'

for comment in user.comments.new(limit=None):
    if comment.subreddit != target_subreddit:
        continue

    print(comment.body)

    if any(x in comment.body for x in ['Sadboi']):
        comment.edit(' ')
