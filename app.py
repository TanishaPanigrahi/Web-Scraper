from flask import Flask, request, jsonify , render_template
from web import crawl_webpage, search_for_keywords
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')



# Define the API Endpoint
@app.route('/crawl' , methods=['POST'])
def find():
    u = request.form['u']
    d1 = request.form['a']
    d2 = request.form['b']
    d3 = request.form['c']
    d4 = request.form['d']
    keywords_to_search = np.array([[d1,d2,d3,d4]])

    # data = request.get_json()
    url = u

  
    content = crawl_webpage(url)

    # keywords_to_search = ["gun", "weapon", "firearm", "ammunition"]

    # Modify this line in your Flask code
    found_keywords = search_for_keywords(content, keywords_to_search[0].tolist())

      
    return render_template('after.html',data=found_keywords)

if __name__ == '__main__':
    app.run(debug=True)