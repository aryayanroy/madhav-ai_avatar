from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/process_transcript', methods=['POST'])
def process_transcript():
    transcript = "Your request is"+request.form['transcript']
    return transcript

if __name__ == '__main__':
    app.run(debug=True)
