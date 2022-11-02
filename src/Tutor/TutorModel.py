from sqlalchemy import DATE, Column,Integer,String
from sqlalchemy.orm import relationship
from base import Base
class Tutor(Base):
    __tablename__ = "Tutor"
    id = Column(Integer,primary_key = True,autoincrement = True)
    first_name = Column('first_name',String(60))
    last_name = Column('last_name',String(60))
    user_email = Column('user_email',String(50))
    whatsapp_number = Column('whatsapp_number',String(50))
    user_password = Column('user_password',String(250))
    tag_id = Column("tag_id",Integer)
    status = Column("status",String(40))


    def __init__ (self,first_name,last_name,user_email,user_password,whatsapp_number,tag_id,status):
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = user_email
        self.user_password = user_password
        self.whatsapp_number_number = whatsapp_number
        self.tag_id = tag_id
        self.status = status
