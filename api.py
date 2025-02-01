from flask import Flask, jsonify
from models import Assignment, db  # Make sure models.py defines your Assignment model and db instance
from schemas import AssignmentSchema  # Optional: If using Marshmallow for serialization

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///assignment_data.db"
db.init_app(app)

# If you are using Marshmallow for serialization, instantiate the schema.
# If not, you can alternatively define a serialize method in your model.
assignment_schema = AssignmentSchema(many=True)

@app.route("/assignments", methods=["GET"])
def get_assignments():
    # Query all assignments from the database.
    assignments = Assignment.query.all()
    # Serialize the data using Marshmallow (or your own method)
    return jsonify(assignment_schema.dump(assignments))

if __name__ == "__main__":
    app.run(debug=True)
