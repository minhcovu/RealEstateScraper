from setuptools import setup, find_packages

setup(
    name="real_estate_scraper",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "beautifulsoup4",
        "sqlalchemy",
        "fastapi",
        "uvicorn",
    ],
    entry_points={
        "console_scripts": [
            "real_estate_scraper = real_estate_scraper.main:main"
        ],
    },
)