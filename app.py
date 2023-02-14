import json

from flask import Flask, request, jsonify
import requests

response=requests.get('https://dev.ylytic.com/ylytic/test').json()['comments']

app=Flask(__name__)

@app.route('/search',methods=['GET'])
def author_name():
    param=request.args
    author_name=param.get("search_author")
    lst_obj = []
    for i in range(len(response)):
        individual_comment = response[i]
        author = individual_comment['author']
        if (author.__contains__(author_name)):
            lst_obj.append({
                "at": individual_comment['at'],
                "author": individual_comment['author'],
                "like": individual_comment['at'],
                "reply": individual_comment['reply'],
                "text": individual_comment['text']
            })
        json_data = json.dumps(lst_obj, sort_keys=True, indent=4)
    return (json.loads(json_data))

