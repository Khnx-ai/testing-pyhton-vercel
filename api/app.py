from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World! Flask app deployed on Vercel.")

@app.route('/greet/<name>')
def greet(name):
    return jsonify(message=f"Hello, {name}! Welcome to the Flask app on Vercel.")

# Vercel requires this to be the entry point
if __name__ == "__main__":
    app.run(debug=True)
