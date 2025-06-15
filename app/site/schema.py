from typing import Optional
from app.core.base_schema import BaseSchema
from app.core.entities.students_model import StudentsModel


class StudentSchema(BaseSchema):
    id: Optional[int] = None
    first_name: str
    last_name: str
    second_name: str
    department: str
    
    @staticmethod 
    def to_entity(schema: "StudentSchema") -> StudentsModel:
        return StudentsModel(
            first_name=schema.first_name,
            last_name=schema.last_name,
            second_name=schema.second_name,
            department=schema.department
        )