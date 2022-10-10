from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSON

from app import Base, session

class Inquiry(Base):
    __tablename__ = 'inquiry'

    id = Column('id',Integer, primary_key=True)
    name = Column('name',String(255), nullable=False)
    requested_at = Column('requested_at',DateTime, nullable=True)
    wants_email = Column('wants_email',String(255), nullable=False) #--> "true|false"
    requester = Column('requester',String(225), nullable=False) #--> requester's email
    status = Column('status',String(255), nullable=False) #--> "received|done|failed|sent"
    
    def __repr__(self):
        return f'Inquiry #{ self.id }: { self.name } requested by { self.requester }'
    
    def save(self):
        session.add(self)
        session.commit()

    def update(self):
        session.commit()

    def remove(self):
        session.delete(self)
        session.commit()

    @classmethod
    def get_by_id(self, id):
        return session.query(Inquiry).filter_by(id=id).first()



class InquiryDetails(Base):
    __tablename__ = 'inquiry_details'

    id = Column('id', Integer, primary_key=True)
    inquiry_id = Column('inquiry_id', Integer, ForeignKey('inquiry.id'))
    nik = Column('nik', String(16), nullable=False)
    status = Column('status', String(255), nullable=False) #--> "received|done|failed|sent"
    response = Column('response', JSON) #--> FDC API's JSON response

    def __repr__(self):
        return f'Inquiry #{self.inquiry_id}: { self.nik }'

    def save(self):
        session.add(self)
        session.commit()

    def update(self):
        session.commit()

    def remove(self):
        session.delete(self)
        session.commit()
