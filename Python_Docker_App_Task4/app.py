from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from your Dockerized Python web server! This is the Credit task of Deployment 4 of Semester 2, 2025"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
