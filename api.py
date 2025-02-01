from flask import Flask, jsonify
from models import Assignment, db  # Ensure models.py defines your Assignment model and db instance
from schemas import AssignmentSchema  # Ensure schemas.py defines AssignmentSchema

# Create the Flask application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///assignment_data.db"

# Initialize the database with the Flask app
db.init_app(app)

# Create an instance of the schema for serializing assignments
assignment_schema = AssignmentSchema(many=True)

# Define a route to fetch assignments
@app.route("/assignments", methods=["GET"])
def get_assignments():
    assignments = Assignment.query.all()
    return jsonify(assignment_schema.dump(assignments))

# Ensure the Flask app runs only when executed directly
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
