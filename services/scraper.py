import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session

import httpx





brand_list = [
    "Toyota", "Honda","Ford","Mercedes","Chevrolet","Nissan", "Volkswagen","BMW", "Tesla"
    ,"Hyundai", "Kai","Mazda","Audi","Lexus","Subaru","Volvo"
]




url = f"https://en.wikipedia.org/wiki/Toyota_Highlander"
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
            elif "seats" in key:
                specs["seats"] = value
            elif "torque" in key:
                specs["torque"] = value
            elif "wheelbase" in key:
                specs["wheelbase" ] = value
            elif "suspension" in key:
                specs["suspension"] = value
            elif "top_speed" in key:
                specs["top_suspension"] = value
            elif "wheelbase" in key:
                specs["wheelbase"] = value
            elif "tires" in key:
                specs["tires"] = value
            elif "drivetrain" in key:
                specs["drivetrain"] = value
            elif "cargo_capacity" in key:
                specs["cargo_capacity"] = value
            elif "height" in key:
                specs["height"]  = value
            elif "length" in key:
                specs["length"] = value
            elif "width" in key:
                specs["width"] = value

    img_tag = table.find("img")
    if img_tag :
        src = img_tag.get("src")
        if src:
            if src.startswith("//"):
                src = "https:" + src
            elif src.startswith("/"):
                src = "https://enwikipedia.org"+src
            img_url = src
    if img_url:
        specs["image_url"] = img_url    
    
    spec ={}
    seen = set()
    like =["engine", "power", "length", "performance", "torque", "acceleration", "transmission"
           , "wheelbase", "width", "height", "battery", "body_type" , "fuel_type", "suspension","seats",
           "top_speed" ,"weight",""           
           ]
    
    for tables in soup.find_all("table", {"class":["wikitable","infobox"]}):
        
       

        for row in tables.find_all("tr"):
                
                cells = row.find_all(["th","td"]) 
                if len(cells) >=2:
                    key= cells[0].get_text(" ", strip=True).lower()
                    val = cells[1].get_text(" ", strip=True)
                    
                   
                    if key not in seen and any(k in key.lower() for k in like):
                        
                        spec[key] = val
                        seen.add(key)
                        
                      
                    
                        
                        

    for key, value in spec.items():
        print(f"{key}: {value}")
    print(specs["image_url"])
   
    



if __name__ == "__main__":
    scrape_wiki_specs(url)