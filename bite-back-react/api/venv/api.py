from flask import Flask

app = flask(__name__)

@app.route('/api/route')
def predict():
    return{'accuracy': 27}