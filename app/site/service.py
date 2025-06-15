from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.entities.students_model import StudentsModel
from app.site.schema import StudentSchema


async def get_students_async(session: AsyncSession) -> list[StudentsModel]:
    students = (await session.execute(select(StudentsModel))).scalars().all()
    
    return list(students)

async def create_student_async(student: StudentSchema, session: AsyncSession):
    student_model = StudentSchema.to_entity(student)
    
    session.add(student_model)
    await session.commit()
    
async def update_student_async(id: int, student: StudentSchema, session: AsyncSession):
    student_model = await _get_student_by_id_async(id, session)

    if not student_model:
        return {"status": "notFound"}

    student_model.last_name = student.last_name
    student_model.first_name = student.first_name
    student_model.second_name = student.second_name
    student_model.department = student.department

    await session.flush()
    await session.commit()

    return {"status": "ok"}

async def delete_student_async(id: int, session: AsyncSession):
    delete_student = await _get_student_by_id_async(id, session)
    
    if not delete_student:
        return {"status": "not_found"}
    
    await session.delete(delete_student)
    await session.commit()
    
    return {"status": "ok"}

async def _get_student_by_id_async(id: int, session) -> StudentsModel | None:
    return (await session.execute(select(StudentsModel).where(StudentsModel.id == id))).scalar()
    