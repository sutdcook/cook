from sqlalchemy import Column ,Integer ,  String , ForeignKey

from models.database import Base
class dish(Base)
    __tablename__ = 'dish'
    id= Column(Integer, primary_key=True)

