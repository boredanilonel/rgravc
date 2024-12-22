from flask import Flask

app = Flask(name)

@app.route('/')
def home():
    return "Hello, Jenkins! This is your app running in Docker."

if name == 'main':
    app.run(host='0.0.0.0', port=8081)