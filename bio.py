#FLASK
from flask import Flask, jsonify, render_template, request
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

@app.route("/")
def about():
    return render_template("index.html", info=info)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    app.run(host="0.0.0.0",debug=debug)