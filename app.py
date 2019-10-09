#FLASK
from flask import Flask, jsonify, render_template, request, send_file
app = Flask(__name__)
import os,optparse
import yaml

# developer = os.getenv("DEVELOPER", "Me")
environment=os.getenv("ENVIRONMENT","development")

with open("links.yaml", 'r',encoding='utf-8') as stream:
    try:
        info = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

picture = info['picture']
name = info['name']
shortbio = info['shortbio']
print(info['picture'])
print(info['name'])
print(info['shortbio'])

social = []
for i in range(len(info['social'])):
    if info['social'][i].get(i).get('enable') == True:
        social.append(info['social'][i].get(i))
    #print(info['social'][i].get(i))

links = []
for i in range(len(info['links'])):
    if info['links'][i].get(i).get('enable') == True:
        links.append(info['links'][i].get(i))   
    #links.append(info['links'][i].get(i))
    #print(info['links'][i].get(i))

@app.route("/")
def about():
    return render_template("index.html", picture=picture, 
    name=name, 
    shortbio=shortbio,
    social=social,
    links=links)

@app.route("/link", methods=['POST'])
def addLink():
    print(request.headers.get('User'))
    if(request.headers.get('User') == 'andr' and request.headers.get('Pass') == '1234'):
        print(request.get_json().get('link'))
        links.append(request.get_json().get('link'))
        return {'response' : "link added correctly"}
    else:
        return {'response': "could not add the link incorrect credentials"}
    print(request.form.to_dict())

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "./CV_Final.pdf"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",port=5000,debug=False)