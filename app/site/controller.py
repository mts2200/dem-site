from pathlib import Path
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config.db import get_sessions_async
from app.site.schema import StudentSchema
from app.site.service import create_student_async, delete_student_async, get_students_async, update_student_async


router = APIRouter(tags=['site'])
static_path = Path(__file__).parent

templates = Jinja2Templates(directory=static_path)

@router.get("/")
async def get_site(request: Request, session: AsyncSession = Depends(get_sessions_async)):
    students = await get_students_async(session)
    
    students_dict = [student.to_dict() for student in students]
    
    print(students_dict)
    
    return templates.TemplateResponse("site.html", context={"request": request, "students": students_dict})

@router.post("/students")
async def create_student(student: StudentSchema, request: Request, session: AsyncSession = Depends(get_sessions_async)):
    await create_student_async(student, session)
    
    students = await get_students_async(session)
    
    students_dict = [student.to_dict() for student in students]
    
    print(students_dict)
    
    return templates.TemplateResponse("site.html", context={"request": request, "students": students_dict})
    
@router.put("/students/{id}")
async def update_student(id: int, student: StudentSchema, request: Request, session: AsyncSession = Depends(get_sessions_async)):
    return await update_student_async(id, student, session)

@router.delete("/students/{id}")
async def delete_student(id: int, request: Request, session: AsyncSession = Depends(get_sessions_async)):
    return await delete_student_async(id, session)