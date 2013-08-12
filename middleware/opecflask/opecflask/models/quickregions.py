from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from database import Base
from opecflask import app
import datetime

class QuickRegions(Base):
   __tablename__ = 'quick_regions'
   id = Column(Integer, index=True, primary_key=True)
   user_id = Column(Integer, ForeignKey('user.id'))
   quickregions = Column(String, unique=False)
   version = Column(Float, unique=False)
   last_used = Column(DateTime, unique=False)

   def __init__(self, user_id=None, quickregions=None):  
      self.user_id = user_id   
      self.quickregions = quickregions
      self.version = app.config['API_VERSION']
      self.last_used = datetime.datetime.now()

   def __repr__(self):
      return '<State ID %r>' % (self.id)