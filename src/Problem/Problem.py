from sqlalchemy import DATE, Column,Integer,String
from sqlalchemy.orm import relationship
from base import Base
class Problem(Base):
    __tablename__ = "Problem"
    id = Column(Integer,primary_key = True,autoincrement = True)
    title = Column('title',String(60))
    description = Column('description',String(60))
    course_tag = Column('course_tag',String(50))
    status = Column("status",String(40))


def __init__ (self,title,description,course_tag,status):
        self.title = title
        self.description = description
        self.course_tag = course_tag
        self.status = status
