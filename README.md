# Car-arena
A backend API for managing car brands, models, and specifications (2018-2025) using FastAPI and SQLAlchemy.

## Features
- Fetch and store car brand from NHTSA API (last 20 models).
- Scrape car specifications and images from wikipedia.
- Store all data in a SQLAlchemy supported database.
- Fast API endpoints to query brands, models, and specs

## Installation
1. Clone the repo.
```bash

git clone https://github.com/yourusername/car-arena.git
cd car-arena
```
2. Create a vitrual enviroonment
```bash
python -m venv venv
source venv/bin/activate         #Linux/macOS
venv\Scripts\activate            #Windows
```
3. Install dependencies:
```bash
pip nstall -r requirements.txt
```
4. Configure database
    - Edit database.py or use a .env file to set your DB URL.
      

## Usage

1. Populate the database:
```bash
cd app
python sea.py
```
2. Run the FastAPI server
``` bash

uvicorn main:app --reload
```

