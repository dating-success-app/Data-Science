"""
Main application and routing logic for Twitoff
"""
from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields


# Define the Application as a Flask App
flask_app = Flask(__name__)

# Use Api to intialize the application. 
app = Api(
    app=flask_app,
    version='0.1',
    title='Dating Description Quality',
    description='Determine how well a description fits a paradigm'         
)

model = app.model('Input Model', 
                    {'text': fields.String(required = True, 
					 description="User input text", 
					 help="cannot be blank.")})

@app.route("/")
class MainClass(Resource):
    def post(self):
        try:
            input_data = request.json
            data = [val for val in input_data.values()]

            score = len(str(data))

            response = jsonify(
                {"statusCode": 200,
				"status": "User description fit",
				"result": score}
            )
            return response

        except Exception as error:
            return jsonify(
                {"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)}
            )



