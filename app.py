from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

    result = 1 if (a + b) > 5.8 else 0

    return jsonify({
        "prediction": result,
        "features": {"a": a, "b": b}
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
