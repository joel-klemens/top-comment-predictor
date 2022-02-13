import sys
import praw
from decouple import config

# subreddit we will get data from
subreddit = 'books'

# env variables to hide login info, global reddit object
# reddit = praw.Reddit(
#     client_id=config('CLIENTID'),
#     password=config('PASSWORD'),
#     username=config('USERNAME'),
#     client_secret=config('CLIENTSECRET'),
#     user_agent='<HalfBloodBot1.0>'
# )

def print_top_comment(submission):
    # Set comment sort to best before retrieving comments
    submission.comment_sort = 'hot'
    # Limit to 1
    submission.comment_limit = 1
    # Fetch the comments and print each comment body
    # This must be done _after_ the above lines or they won't take affect.
    # open a file we will print the data we gather to
    with open('data/' + 'funny' + '.txt', 'a', encoding="utf-8") as f:
        # anything printed will now go into this file
        sys.stdout = f
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, praw.models.MoreComments):
                continue
            if (top_level_comment.stickied == True):
                continue
            # Here you can fetch data off the comment.
            # For the sake of example, we're just printing the comment body.
            print(submission.title + ' ' + top_level_comment.body)


def top_posts_from_subreddit(sub_name):
    subreddit = reddit.subreddit(sub_name)
    top_posts = []
    # The default for the 'top' function is "top of all time".
    # this should gather 1000 posts and top comments
    for post in subreddit.top():
        top_posts.append(post)
    return top_posts


# start adding to the file
posts = top_posts_from_subreddit(subreddit)
for post in posts:
    print_top_comment(post)
