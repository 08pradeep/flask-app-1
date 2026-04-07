from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return [200~"Welcome to My Updated Flask App"

app.run(host='0.0.0.0', port=5000)
