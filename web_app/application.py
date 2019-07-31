"""
Main application and routing logic for Twitoff
"""
from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields


# Define the Application as a Flask App
application = Flask(__name__)

# Use Api to intialize the application. 
# app = Api(
#     app=flask_app,
#     version='0.1',
#     title='Dating Description Quality',
#     description='Determine how well a description fits a paradigm'         
# )

# model = app.model('Input Model', 
#                     {'text': fields.String(required = True, 
# 					 description="User input text", 
# 					 help="cannot be blank.")})

@application.route('/')
def default():
    return 'Homepage'

@application.route("/api", methods=['POST'])
def predict():

    try:
        input_data = request.get_json(force=True)
        data = input_data['description']

        score = len(str(data))

        response = jsonify(
            {"score": score}
        )
        return response

    except Exception as error:
        return jsonify(
            {"statusCode": 500,
            "status": "Check JSON format",
            "error": str(error)}
        )
if __name__ == '__main__':
   application.run()

