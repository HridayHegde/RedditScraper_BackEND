from flask import Flask, request
from Main import scrapper
#from flask import Flask, render_template, request, redirect, url_for, send_from_directory,jsonify



app = Flask(__name__)

@app.route("/getfromreddit", methods=['POST'])
def getfromreddit():
    some_json=request.get_json()
    limit = some_json['limits']
    subreddit = some_json['subreddit']  
    print(subreddit)
    response = scrapper.Scrape(subred=subreddit,limits=limit) 
    return response

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=False)
