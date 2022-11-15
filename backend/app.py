from flask import Flask, request
from json import load 
from re import sub

replies = {}
with open('langTree.json') as f:
    replies = load(f)


app = Flask(__name__)

@app.post('/text')
def reply():
    global replies
    if request.content_type == "application/json":
        check = request.json["sentence"]
        print(check)
        check = sub("[':;-]" , '', check)
        check = sub('[,\.\?"!]',' ',check)
        #chunk = sorted([i.lower() for i in check.split()])
        chunk = [i.lower() for i in check.split()]
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
                    return(x[delim][0])
                    print("Correct:",x[delim][1])
                    break
        else:
            while not delim in x:
                for i in x:
                    x = x[i]
                    break
            print("Correct:",x[delim][1])
            return(x[delim][0])
    else:
        return "Unable to understand request"
