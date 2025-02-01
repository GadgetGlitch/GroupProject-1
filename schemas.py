from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Assignment

class AssignmentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Assignment
        load_instance = True
