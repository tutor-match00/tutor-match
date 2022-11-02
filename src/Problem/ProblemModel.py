from sqlalchemy import DATE, Column,Integer,String
from sqlalchemy.orm import relationship
from base import Base
class Problem(Base):
    __tablename__ = "Problem"
    id = Column(Integer,primary_key = True ,autoincrement = True)
    title = Column('title',String(60))
    description = Column('description',String(60))
    course_tag = Column('course_tag',String(50))
    status = Column("status",String(40))
    tutee_id = Column("tutee_id",Integer)
    tag_id = Column("tag_id",Integer)


    def __init__ (self,title,description,course_tag,status,tag_id,tutee_id):
        self.title = title
        self.description = description
        self.course_tag = course_tag
        self.status = status
        self.tag_id = tag_id
        self.tutee_id = tutee_id
