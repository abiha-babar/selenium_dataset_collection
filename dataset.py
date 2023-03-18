from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pdb
import urllib
import os

# Define the search queries and folder names
search_queries = ["happy baby", "sad baby", "weeping baby"]
folder_names = ["happy_baby", "sad_baby", "weeping_baby"]

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

# Loop through the search queries
for query, folder_name in zip(search_queries, folder_names):
    # Navigate to Google Images and search for the query
    driver.get("https://www.google.com/imghp")
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys(query)
    search_bar.submit()

    # Create a folder for the images if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Download the first 10 images
    imgs = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
    for i, img in enumerate(imgs[:20]):
        try:
            src = img.get_attribute("src")
            urllib.request.urlretrieve(src, f"{folder_name}/{i}.jpg")
        except:
            pass

# Close the browser
driver.quit()
