from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from fastapi import Query

from typing import Optional, List
from scraper import Scraper
from database import Database
from pydantic import BaseModel, HttpUrl

app = FastAPI()
database = Database()
scraper = Scraper()

class ScrapeRequest(BaseModel):
    url: HttpUrl

@app.post("/scrape")
def scrape(request: ScrapeRequest):
    try:
        listings = scraper.scrape(request.url)
        scraper.export_to_csv("exports/homely_listings.csv", listings)

        for listing in listings:
            database.insert_listing(listing)

        return {"message": f"{len(listings)} listings scraped and stored"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return FileResponse("web/index.html")

@app.get("/listings")
def get_listings(
    id: Optional[List[int]] = Query(None),
    skip: int = 0, 
    limit: int = 50
):
    if id:
        listings = database.get_listing_by_ids(id)
    else:
        listings = database.get_listings_paginated(skip=skip, limit=limit)
    return [l.to_dict() for l in listings]

@app.get("/listings/search")
def search_listings(address: str = Query(...)):
    results = database.search_by_address(address)
    return [l.to_dict() for l in results]

@app.get("/listings/{listing_id}")
def get_listing_by_id(listing_id: int):
    return database.get_listing_by_ids([listing_id])