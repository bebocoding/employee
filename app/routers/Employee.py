from typing import List
import uuid
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..database import get_db
from . import EmployeeLocation

router = APIRouter(
    prefix="/employees",
    tags=['Employee']
)

router.include_router(EmployeeLocation.router)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Token)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    # Hash a password - user.password
    hashed_password = utils.hash(employee.password)
    employee.password = hashed_password

    new_employee = models.Employee(**employee.model_dump())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    access_token = oauth2.create_access_token(
        data={"employee_id": str(new_employee.employee_id)})

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/{id}", response_model=schemas.EmployeeOut)
def get_employee(id: str, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(
        models.Employee.employee_id == id).first()

    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"employee with id {id} does not exist!")
    return employee


@router.get("/", response_model=List[schemas.EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(models.Employee).all()

    return employees


@router.delete("/")
def remove_employee(db: Session = Depends(get_db),
                    current_employee: int = Depends(oauth2.get_current_employee)):

    employee_query = db.query(models.Employee).filter(
        models.Employee.employee_id == current_employee.employee_id)
    employee = employee_query.first()
    if not employee_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"employee with id {current_employee.employee_id} does not exist anymore!")
    employee_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
