import praw
import requests
import datetime
import json

reddit = praw.Reddit(client_id='sUgT5bpF6GiuLg',
                     client_secret='jo_NXKQbDKzFtUgjhaPkZ0dH3ck',
                     user_agent='Chrome:none:v.01 (by /u/Slight_Hunter)',
                     username='Slight_Hunter',
                     password='Slight_Hunter_')

def thread2comments(thread_id):
    thread=reddit.submission(id=thread_id)
    return extract_comments(thread.comments)

def extract_comments(comm_tree, min_size=3):
    comm_dic={}
    for comment in comm_tree:
        if type(comment) is praw.models.reddit.more.MoreComments:
            if comment.count>min_size:
                temp=extract_comments(comment.comments())
                comm_dic.update(temp)
        else:
            comm_dic[comment.id]=comment.body
    return comm_dic

def sub2comms(subname):
    final_dic={}
    try:
        reddit.subreddit(subname).quaran.opt_in()
    except:
        pass
    for submission in reddit.subreddit(subname).hot(limit=1000):
        print(submission.id)
        final_dic[submission.title]=thread2comments(submission.id)
    return final_dic

with open('setup.txt') as f:
    setup = json.load(f)


credentials = setup['credentials']
subreddits = setup['subreddits']
client_id = credentials['client_id']
client_secret = credentials['client_secret']
user_agent = credentials['user_agent']
username = credentials['username']
password = credentials['password']

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)

try:
    i=0
    for subreddit in subreddits:
        print('Subreddit ' + str(i+1) + ' out of ' + str(len(subreddits)))
        text = sub2comms(subreddit)
        i+=1
        print(text)
        print(subreddit)
        with open('test','w') as f:
                f.write(str(subreddit))
        p='OUTPUT' + str(subreddit)+'.json'
        print(p)
        with open(p,'w') as f:
            setup = json.dump(text, f)
except Exception as e:
    print("type error: " + str(e))
    with open('ERROR','w') as f:
            f.write(e)
