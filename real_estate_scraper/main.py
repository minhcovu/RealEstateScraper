import uvicorn

def main():
    uvicorn.run("real_estate_scraper.api:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()