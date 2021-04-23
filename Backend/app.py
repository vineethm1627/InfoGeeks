from flask import Flask, request
import github_module
import youtube_module
import sentiment_analysis
import final_file_parallel
import web_scraper
from flask_cors import CORS, cross_origin

app = Flask(__name__) 
CORS(app, support_credentials=True)

@app.route('/github')
@cross_origin(supports_credentials=True)
def fetch():
    query = request.args.get('query')
    temp = github_module.extract_repos(query)
    return {'URLS':github_module.sortfun(temp)}


@app.route('/youtube')
@cross_origin(supports_credentials=True)
def fetchVideoLinks():
    query = request.args.get('query')
    temp = youtube_module.extractYoutubeVideos(query)
    return {'Videos': temp}


@app.route('/twitter')
@cross_origin(supports_credentials=True)
def fetchTweets():
    query = request.args.get('query')
    temp = sentiment_analysis.get_tweets_main(query)
    return {'Tweets': temp}


@app.route('/webscrape')
@cross_origin(supports_credentials=True)
def fetchLinks():
    query = request.args.get('query')
    temp = web_scraper.links_for_search(query)
    return {'Links': temp}


@app.route('/parallel')
@cross_origin(supports_credentials=True)
def fetchAll():
    query = request.args.get('query')
    temp = final_file_parallel.parallel_implementation(query)
    return temp

if __name__ == '__main__':
   app.run(debug=True, port=5000)