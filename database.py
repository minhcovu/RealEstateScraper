from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from entities import Base, Listing  

class Database:
    def __init__(self, db_url = "sqlite:///real_estate.db"):
        self.engine = create_engine(db_url, echo=True)
        self.session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def insert_listing(self, listing):
        session = self.session()
        try:
            session.add(listing)
            session.commit()
        except Exception as e:
            session.rollback()
            print("Error inserting listing:", e)
        finally:
            session.close()

    def get_all_listings(self):
        session = self.session()
        try:
            return session.query(Listing).all()
        finally:
            session.close()
