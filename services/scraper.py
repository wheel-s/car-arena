import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

import httpx





brand_list = [
    "Toyota", "Honda","Ford","Mercedes","Chevrolet","Nissan", "Volkswagen","BMW", "Tesla"
    ,"Hyundai", "Kai","Mazda","Audi","Lexus","Subaru","Volvo"
]




url = f"https://en.wikipedia.org/wiki/Toyota_Yaris"
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
        header = row.find("th")
        value = row.find("td")
        if header and value:
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
            elif "power" in key or "horsepower" in key:
                specs["horsepower"] = value
            elif "acceleration" in key:
                specs["acceleration"] = value
            elif "transmission" in key:
                specs["transmission"] = value
            elif "Battery" in key:
                specs["Battery"] = value

    img_tag = table.find("a",{"class":"image"})
  
  #  specs["image_url"] = "https:" + img_tag.img.get("src") if img_tag and img_tag.img else None
    
    print(specs)



if __name__ == "__main__":
    scrape_wiki_specs(url)