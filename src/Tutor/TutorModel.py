from sqlalchemy import DATE, Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base


class Tutor(Base):
    __tablename__ = "Tutor"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column('first_name', String(60))
    last_name = Column('last_name', String(60))
    user_email = Column('user_email', String(50))
    whatsapp_number = Column('whatsapp_number', String(50))
    user_password = Column('user_password', String(250))
    course_tag = Column("course_tag", String)

    problems = relationship("Problem", backref="tutor")

    def __init__(self, first_name, last_name, user_email, user_password, whatsapp_number, course_tag):
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.user_password = user_password
        self.whatsapp_number_number = whatsapp_number
        self.course_tag = course_tag
