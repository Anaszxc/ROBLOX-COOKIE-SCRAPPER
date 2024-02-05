
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receive_cookies():
    data = request.json
    if 'cookies' in data:
        cookies = data['cookies']
        # Process the received cookies (e.g., store them in a database)
        print("Received cookies:", cookies)
        return jsonify({"message": "Cookies received successfully"}), 200
    else:
        return jsonify({"error": "No cookies provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)