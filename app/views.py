from flask import Flask, request, render_template
from .match import pattern_matching
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('main.html')

@app.route('/match', methods=['POST'])
def handle_match():
  """Handles pattern matching
  This function only outputs name of pattern if one found
  In the case that no match is found it will output No Match
  """
  content = request.get_json()
  data = content['data']
  res = pattern_matching(data)

  message =  "Found {0}".format(res[1]) if res[0] else "No Match"
  print(message)
  return message

@app.route('/cmatch', methods=['POST'])
def handle_matchnshow():
  """A More complicated version of handle_match
  This function outputs a HTML page containing a table of input matrix
  """
  content = request.get_json()
  data = content['data']

  res = pattern_matching(data)
  df = pd.DataFrame(data)

  message =  "Found {0}".format(res[1]) if res[0] else "No Match"

  return render_template('result.html', dftable=df.to_html(), header_message=message)