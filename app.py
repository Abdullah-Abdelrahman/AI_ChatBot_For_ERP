from flask import Flask, render_template,request,jsonify

from flask_cors import CORS
import chat as c


app = Flask(__name__)
CORS(app)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = c.get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
