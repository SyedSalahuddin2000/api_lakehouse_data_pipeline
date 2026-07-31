import requests
from datetime import datetime
import json
from config import load_config

config = load_config()
url = config["api"]["url"]
timeout = config["api"]["TIMEOUT"]

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

response = requests.get(url)
if response.status_code == 200:
    print("sucess")
    data = response.json()
    with open(f"data/raw/products_{current_time}.json","w") as f:
        json.dump(data,f)
        
else:
    print("Failed to retrieve data. Status code:", response.status_code)