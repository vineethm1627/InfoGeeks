from flask import Flask, request
import github_module
from flask_cors import CORS, cross_origin

app = Flask(__name__) 
CORS(app, support_credentials=True)

@app.route('/github')
@cross_origin(supports_credentials=True)
def fetch():
    query = request.args.get('query')
    temp = github_module.extract_repos(query)
    return {'URLS':github_module.sortfun(temp)}

if __name__ == '__main__':
   app.run(debug=True, port=5000)