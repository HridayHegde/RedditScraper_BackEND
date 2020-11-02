import praw, requests

import json


my_client_id = "ll0MiILrycFxGA"
secret = "latgPA_cig6s3U0wvTIj4DhQB5s"
my_user_agent = "androidminiprojscrapper"

def Scrape(subred = ['memes'],limits = 100):
    outstring = '{"memes":['
    redditinst = praw.Reddit(client_id = my_client_id,client_secret = secret,user_agent = my_user_agent)

    for i,x in enumerate(subred):
        print(i)
        print(len(subred))
        if i != 0:
            outstring = outstring + ","
        top_posts = redditinst.subreddit(x).hot(limit=limits)
        counter = 0
        for d,post in enumerate(top_posts):
            if not post.is_self:
                
                
                if not counter == 0:
                    
                    outstring = outstring+","

            
                #print(post.url)
                #print(post.title)
                title = post.title
                
                title = title.replace('"','')
                #print(title)
                outstring= outstring+ '{ "title":"'+title+'","url":"'+post.url+'"}'
                counter = counter + 1

    outstring = outstring+']}'

    job = json.dumps(outstring)
    print(job)

    return job

        


