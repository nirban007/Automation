from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import os

# Set up the Selenium webdriver
webdriver_service = Service('path_to_chromedriver')
driver = webdriver.Chrome(service=webdriver_service)

# Navigate to the website
url = "https://www.daraz.com.bd/womens-shalwar-kameez/?from=filter&page=2&price=600-&spm=a2a0e.home.cate_1_1.1.735212f7dEHPd6"  # Replace with the URL of the website you want to scrape
driver.get(url)

# Initialize empty lists
prod_titles = []
prod_links = []
prod_images = []
for page in range(1,5):
    

# Extract product titles, links, and images
    for p in range(1, 39):
        k = str(p)
        prod_title_element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[3]/div['+ k +']/div/div/div[1]/div/a')
        prod_title = prod_title_element.text
        prod_titles.append(prod_title)
        
        prod_link = prod_title_element.get_attribute('href')  # Assuming the link is in the href attribute
        prod_links.append(prod_link)
        
        prod_image_element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[1]/div/div[1]/div[3]/div['+ k +']/div/div/div[1]/div/a/img')
        prod_image = prod_image_element.get_attribute('src')
        prod_images.append(prod_image)

        # Save the image
        image_name = f"product_{p}.png"  # Generate a unique name for each image
        image_path = os.path.join("images", image_name)  # Specify the folder path and image name
        prod_image_element.screenshot(image_path)
        print(f"Image {image_name} saved.")

# Store product titles and links in a CSV file
csv_path = "product_data.csv"  # Specify the path to the CSV file
with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link"])  # Write the header row
    for title, link in zip(prod_titles, prod_links):
        writer.writerow([title, link])

# Close the browser
driver.quit()
