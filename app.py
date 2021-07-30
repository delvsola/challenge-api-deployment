from flask import Flask, request, abort, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def _index():
    if request.method == "GET":
        return 'alive', 200


@app.route('/predict', methods=['POST', 'GET'])
def _predict():
    """
    Should receive a JSON object in the GET request with all the
    information about the house.
    :return: Prediction data or error in JSON format
    """
    if request.method == "POST":
        # Parse data and send prediction
        data = request.get_json(force=True).get("data", None)
        if not data:
            return {"error": "Invalid content."}, 400

    elif request.method == "GET":
        resp = "The POST method expects a JSON dictionary with a \"data\" " \
              "key containing a dictionary with the house's specifications." \
              "\n" \
              "e.g.: {\"data\": {\"area\": 100...}}"
        return resp


if __name__ == '__main__':
    app.run()
