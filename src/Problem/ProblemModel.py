from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from Tutor.TutorModel import Tutor
from Tutee.TuteeModel import Tutee


class Problem(Base):
    __tablename__ = "Problem"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(60))
    description = Column('description', String(255))
    course_tag = Column('course_tag', String(50))
    status = Column("status", Boolean)
    # tutee_id = Column("tutee_id", Integer)
    # tutor_id = Column("tutor_id", Integer)
    tutor_id = Column(Integer, ForeignKey(
        Tutor.id, ondelete='CASCADE'))
    tutee_id = Column(Integer, ForeignKey(
        Tutee.id, ondelete='CASCADE'))

    def __init__(self, title, description, course_tag, status, tutee_id):
        self.title = title
        self.description = description
        self.course_tag = course_tag
        self.status = status
        self.tutee_id = tutee_id
