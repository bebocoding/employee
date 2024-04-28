from typing import List
import uuid
from fastapi import Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/locations",
    tags=['Locations']
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.EmployeeLocationOut)
def create_location(employeeLocation: schemas.EmployeeLocationCreate, db: Session = Depends(get_db),
                    current_employee: int = Depends(oauth2.get_current_employee)):

    new_employee_location = models.EmployeeLocation(
        **employeeLocation.model_dump(), employee_id=current_employee.employee_id)
    db.add(new_employee_location)
    db.commit()
    db.refresh(new_employee_location)

    return new_employee_location


@router.get("/{location_id}", response_model=schemas.EmployeeLocationOut)
def get_location(location_id: str, db: Session = Depends(get_db), current_employee: int = Depends(oauth2.get_current_employee)):
    location = db.query(models.EmployeeLocation).filter(
        models.EmployeeLocation.employee_id == current_employee.employee_id,
        models.EmployeeLocation.location_id == location_id).first()

    if not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"location with id {location_id} does not exist!")
    return location


@router.get("/", response_model=List[schemas.EmployeeLocationOut])
def get_employee_locations(db: Session = Depends(get_db), current_employee: int = Depends(oauth2.get_current_employee)):
    locations = db.query(models.EmployeeLocation).filter(
        models.EmployeeLocation.employee_id == current_employee.employee_id).all()

    return locations


@router.put("/{location_id}", response_model=schemas.EmployeeLocationOut)
def update_post(location_id: str, updatedLocation: schemas.EmployeeLocationCreate, db: Session = Depends(get_db),
                current_employee: int = Depends(oauth2.get_current_employee)):

    location_query = db.query(models.EmployeeLocation).filter(
        models.EmployeeLocation.location_id == location_id)
    location = location_query.first()

    if location == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} was not found")
    if location.employee_id != current_employee.employee_id:

        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perfrom the requested action")
    location_query.update(updatedLocation.model_dump(),
                          synchronize_session=False)
    db.commit()

    return location_query.first()


@router.delete("/{location_id}")
def remove_employee_location(location_id: str, db: Session = Depends(get_db), current_employee: int = Depends(oauth2.get_current_employee)):

    location_query = db.query(models.EmployeeLocation).filter(
        models.EmployeeLocation.employee_id == current_employee.employee_id,
        models.EmployeeLocation.location_id == location_id)

    location = location_query.first()
    if not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"location with id {location_id} does not exist!")
    location_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
