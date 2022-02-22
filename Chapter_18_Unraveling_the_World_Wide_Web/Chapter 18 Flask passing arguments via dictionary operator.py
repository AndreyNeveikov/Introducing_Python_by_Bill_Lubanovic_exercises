from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/echo/')
def echo():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['place'] = request.args.get('place')
    return render_template('flask_template.html', **kwargs)


app.run(port=6789, debug=True)
