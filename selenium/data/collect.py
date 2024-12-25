import os
from bs4 import BeautifulSoup
import pandas as pd

d = {'title': [], 'price': [], 'link': []}

# Path to the folder containing the HTML files
folder_path = "data"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Only process files with .html extension
    if os.path.isfile(file_path) and filename.endswith(".html"):
        print(f"Processing file: {filename}")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                html_doc = file.read()
            soup = BeautifulSoup(html_doc, "html.parser")

            # Locate the main product container
            product_div = soup.find("div", class_="tUxRFH")
            if product_div:
                # Extract the <a> tag containing the title and link
                link_tag = product_div.find("a", class_="CGtC98")
                if link_tag:
                    title = link_tag.find("div", class_="KzDlHZ").get_text(strip=True)  # Product title
                    link = "https://www.flipkart.com" + link_tag["href"]  # Product link
                    print("Title:", title)
                    print("Link:", link)
                else:
                    print("No link tag found in the product container.")
            else:
                print("No product container found.")
            


            p = soup.find(attrs={"class" : 'Nx9bqj _4b5DiR'})
            price = (p.get_text())
            d['title'].append(title)
            d['link'].append(link)
            d['price'].append(price)
        except Exception as e:
            print(e)

df = pd.DataFrame(data = d)
df.to_csv("data.csv")



