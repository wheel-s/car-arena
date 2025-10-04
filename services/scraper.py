import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from app import models, database
import httpx



models.Base.metadata.create_all(bind=database.engine)
db:Session = database.SessionLocal()




brand_list = [
    "Toyota", "Honda","Ford","Mercedes","Chevrolet","Nissan", "Volkswagen","BMW"
    ,"Hyundai", "Kai","Mazda","Audi","Lexus","Subaru","Volvo"
]




url = f"https://en.wikipedia.org/wiki/Toyota_Auris"
headers = {
        "useAgent":"CarSpecScraper/0.1 (contact:toshirou2002@gmail.com)"
    
    }
def scrape_wiki_specs(url):
    response = httpx.get(url, headers=headers)
    
    if response.status_code!=200:
        print("not sucessful")
        return None
    soup = BeautifulSoup(response.text, "html.parser")

    specs={}

    table = soup.find("table", class_=lambda x:x and"infobox" in x)
   
    if not table:
        print("table not found")
        return None


    for row in table.find_all("tr"):
        if row.th and row.td:
            key = row.th.get_text(strip=True).lower()
            value = row.td.get_text(strip=True)
            if "engine" in key:
                specs["engine"] = value
            elif "fuel" in key:
                specs["fuel_type"] =value
            elif "body" in key :
                specs["body_type"] = value
            elif "weight" in key:
                specs["weight"] = value

    img_tag = table.find("a",{"class":"image"})
  
  #  specs["image_url"] = "https:" + img_tag.img.get("src") if img_tag and img_tag.img else None
    
    print(specs)



if __name__ == "__main__":
    scrape_wiki_specs(url)