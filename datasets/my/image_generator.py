import requests
import os

"""
ACCESS_KEY = "YOUR_UNSPLASH_ACCESS_KEY"
query = "shirts"
per_page = 30

url = f"https://api.unsplash.com/search/photos?query={query}&per_page={per_page}&client_id={ACCESS_KEY}"
response = requests.get(url).json()

os.makedirs(query, exist_ok=True)

for i, photo in enumerate(response["results"]):
    image_url = photo["urls"]["regular"]
    img_data = requests.get(image_url).content
    with open(f"{query}/{query}_{i}.jpg", "wb") as f:
        f.write(img_data)

print("Download complete!")
"""



import requests
import os

API_KEY = "3tG4ZqF3srDqaIcGNkEtHOHKNIgtZmLxsdg3DIALAjZsDAagw7sazrZ5" #pexels API


headers = {
    "Authorization": API_KEY
}

categories = {
    "shirts": "only shirts or t-shirts no men or women photos wearing.",
    "pants": "jeans OR trousers OR chinos only these photos no model wearing.",
    "footwear": "sneakers OR shoes OR boots , one image should contain only one pair of footwear",
    "accessories": "watch OR sunglasses OR handbag OR cap , one image should contain only one accessories"
}

"""
categories = {
    "shirts": "shirt OR t-shirt, single item, flat lay product photography, isolated on white background OR wooden table, no model, no person, no wearing, only clothing item",
    "pants": "jeans OR trousers OR chinos, single item, neatly placed, product photography, isolated, no model, no person, no wearing, only pants",
    "footwear": "single pair of sneakers OR shoes OR boots, product photography, isolated on clean background, only one pair, no model, no person, no wearing",
    "accessories": "single watch OR sunglasses OR handbag OR cap, product photography, isolated background, only one item, no model, no person"
}
"""
IMAGES_PER_CATEGORY = 50   # Change this number as needed

def download_images(category, query):
    os.makedirs(category, exist_ok=True)
    
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=80"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Error:", response.status_code)
        return
    
    data = response.json()
    photos = data["photos"]
    
    count = 0
    
    for photo in photos:
        if count >= IMAGES_PER_CATEGORY:
            break
            
        img_url = photo["src"]["large"]
        img_data = requests.get(img_url).content
        
        with open(f"{category}/{category}_{count}.jpg", "wb") as f:
            f.write(img_data)
        
        count += 1
    
    print(f"{category} downloaded successfully!")

for category, query in categories.items():
    download_images(category, query)

print("All downloads completed.")
