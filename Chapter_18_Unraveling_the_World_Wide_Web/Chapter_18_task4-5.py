# 4
"""Template created"""


#5
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    thing = request.args.get('thing')
    height = request.args.get('height')
    color = request.args.get('color')
    return render_template("home.html", thing=thing, height=height, color=color)


app.run(port=5000, debug=True)

#http://127.0.0.1:5000/?thing=Book&height=20cm&color=white
