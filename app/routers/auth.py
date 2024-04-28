from fastapi import APIRouter, status, Depends, Response, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, utils, oauth2

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login', response_model=schemas.Token)
def login(user_credentials: schemas.EmployeeLogin, db: Session = Depends(get_db)):
    # Authenticate the user
    employee = db.query(models.Employee).filter(
        models.Employee.username == user_credentials.username).first()

    if employee == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Invalid Credentials')
    if not utils.verify(user_credentials.password, employee.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Invalid Credentials')
    # Create a token
    access_token = oauth2.create_access_token(
        data={"employee_id": str(employee.employee_id)})
    # return token
    return {"access_token": access_token, "token_type": "bearer"}
