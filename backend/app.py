from flask import Flask, request
from json import load 

replies = {}
with open('langTree.json') as f:
    replies = load(f)


app = Flask(__name__)

@app.post('/text')
def reply():
    global replies
    if request.content_type == "application/json":
        check = request.json[ "sentence"]
        print(check)
        chunk = sorted([i.lower() for i in check.split()])
        delim = '&&'
        x = replies
        for i in chunk:
            if i in x:
                x = x[i]
            else:
                for j in x:
                    if not j == delim:
                        x = x[j]
                        break
                else:
                    return(x[delim])
                    break
        else:
            while not delim in x:
                for i in x:
                    x = x[i]
                    break
            return(x[delim])
    else:
        return "Unable to understand request"
