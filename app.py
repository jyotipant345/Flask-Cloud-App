
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Cloud Application!</h1>
    <h2>Python Flask Application</h2>
    <p>This application is deployed on the cloud.</p>
    <p>Cloud Computing Practical</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
