from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/<path:path>')
def catch_all(path):
    return "Thank you " + path + "! But our princess is in another castle!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
