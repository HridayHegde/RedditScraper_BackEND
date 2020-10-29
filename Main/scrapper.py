import praw, requests

import json


my_client_id = "ll0MiILrycFxGA"
secret = "latgPA_cig6s3U0wvTIj4DhQB5s"
my_user_agent = "androidminiprojscrapper"

def Scrape(subred = ['memes'],limits = 100):
    outstring = "{'memes':["
    redditinst = praw.Reddit(client_id = my_client_id,client_secret = secret,user_agent = my_user_agent)

    for i,x in enumerate(subred):
        if not i == 0:
            outstring = outstring + ","
        top_posts = redditinst.subreddit(x).hot(limit=limits)
        for i,post in enumerate(top_posts):
            if not i == 0:
                outstring = outstring+","

            if not post.is_self:
                #print(post.url)
                #print(post.title)
                outstring= outstring+ "{ 'title':'"+post.title+"','url':'"+post.url+"'}"

    outstring = outstring+"]}"

    job = json.dumps(outstring)

    return job

        


