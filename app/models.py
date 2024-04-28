import uuid
from .database import Base, engine
from sqlalchemy import TIMESTAMP, Column, Float, Integer, String, Boolean, text, ForeignKey, UUID
from sqlalchemy.orm import relationship


class EmployeeLocation(Base):
    __tablename__ = "EmployeeLocations"

    location_id = Column(UUID(as_uuid=True), primary_key=True,
                         nullable=False, default=uuid.uuid4)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    image_path = Column(String)
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False,
                       server_default=text('now()'))
    employee_id = Column(UUID, ForeignKey(
        "Employees.employee_id", ondelete="CASCADE"), nullable=False)


class Employee(Base):
    __tablename__ = "Employees"
    employee_id = Column(UUID(as_uuid=True), primary_key=True,
                         nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    position = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
