"""
Main application and routing logic for Datify
"""
from flask import Flask, request, jsonify
from paradigm import load_models

# Define the Application as a Flask App
application = Flask(__name__)


@application.route('/')
def default():
    return 'Homepage'

@application.route("/api", methods=['POST'])
def predict():

    try:
        input_data = request.get_json(force=True)
        data = input_data['description']
        #run models
        score = load_models([data])
        #returns a JSON
        response = jsonify(
            {"score": score}
        )
        return response

    except Exception as error:
        return jsonify(
            {"statusCode": '?',
            "status": "Check JSON format",
            "error": str(error)}
        )
if __name__ == '__main__':
   application.run()

