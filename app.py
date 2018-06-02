from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome! This is a Sample Flask app."

if __name__ == "__main__":
    app.run(debug=True)