from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from entities import Base, Listing  
from typing import List

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

    def get_listings_paginated(self, skip=0, limit=50):
        session = self.session()
        try:
            return session.query(Listing).offset(skip).limit(limit).all()
        finally:
            session.close()

    def get_listing_by_ids(self, ids: List):
        session = self.session()
        try:
            return session.query(Listing).filter(Listing.id.in_(ids)).all()
        finally:
            session.close()

    def search_by_address(self, address_substring: str):
        session = self.session()
        try:
            return session.query(Listing)\
                .filter(Listing.address.ilike(f"%{address_substring}%"))\
                .all()
        finally:
            session.close()