from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth, Employee
from . import models


# no need for table creating after alembic :D
models.Base.metadata.create_all(bind=models.engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Employee.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello employee"}
