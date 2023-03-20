from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import urllib
import os
import time
import pdb

target = int(input("Enter the total number of pictures you want to download for [HAPPY BABY, SAD BABY, WEEPING BABY] :: "))

# Define the search queries and folder names
search_queries = ["happy baby", "sad baby", "weeping baby"]

driver = webdriver.Chrome(ChromeDriverManager().install())

# Loop through the search queries
for query in search_queries:
    total = 0

    # Navigate to Google Images and search for the query
    folder_name = query.replace(" ", "_")
    main_folder = folder_name

    if not os.path.exists(main_folder):
        os.makedirs(main_folder)

    sub_folders = ["American", "British", "Canadian", "Mexican", "Argentinean", "Brazilian", "Chilean", "Colombian", "Peruvian", "Venezuelan", "French", "German", "Italian", "Spanish", "Portuguese", "Dutch", "Swedish", "Norwegian", "Danish", "Finnish", "Icelandic", "Russian", "Polish", "Ukrainian", "Czech", "Slovak", "Hungarian", "Romanian", "Bulgarian", "Greek", "Turkish", "Israeli", "Iranian", "Iraqi", "Syrian", "Saudi Arabian", "Lebanese", "Egyptian", "Moroccan", "Tunisian", "Algerian", "Nigerian", "South African", "Kenyan", "Ugandan", "Ghanaian", "Ivorian", "Senegalese", "Cameroonian", "Ethiopian", "Somalian", "Sudanese", "Chinese", "Japanese", "Korean", "Thai", "Vietnamese", "Indian", "Pakistani", "Bangladeshi", "Sri Lankan", "Nepalese", "Cambodian", "Indonesian", "Filipino", "Australian", "New Zealander", "Fijian", "Papua New Guinean", "Tongan", "Samoan", "Tuvaluan", "Kiribati", "Micronesian", "Marshallese", "Palauan", "Solomon Islander", "Tuvaluan", "Vanuatuan", "Cook Islander", "Niuean", "American Samoan", "Afghan", "Kuwaiti", "Qatari", "Emirati", "Omani", "Bahraini", "Yemeni", "Jordanian", "Palestinian", "Mongolian", "North Korean", "Taiwanese", "Laotian", "Singaporean", "Malaysian", "Bruneian", "Myanmar/Burmese", "Bhutanese", "Mauritian", "Malagasy", "Seychellois", "Mauritanian", "Namibian", "Botswanan", "Zambian", "Zimbabwean", "Mozambican"]

    not_related_to_baby = ["Deadstock", "Horsman", "Doll", "African American", "Pink dress", "eBay", "Vintage", "Collectible", "Toy", "Figurine", "Miniature", "Statue", "Sculpture", "Art", "Craft", "Handmade", "Souvenir", "Memorabilia", "Gift", "Decoration", "Ornament", "Home decor", "Display", "Showcase", "Cabinet", "Shelf", "Curio", "Trinket", "Knick-knack", "Bauble", "Novelty", "Gadget", "Accessory", "Jewelry", "Gemstone", "Bead", "Charm", "Pendant", "Necklace", "Bracelet", "Earring", "Ring", "Watch", "Sunglasses", "Fashion", "Style", "Trend", "Design", "Pattern", "Texture", "Color", "Material", "Fabric", "Leather", "Fur", "Velvet", "Silk", "Cotton", "Linen", "Wool", "Metal", "Wood", "Glass", "Ceramic", "Porcelain", "Stone", "Marble", "Granite", "Brick", "Concrete", "Architecture", "Interior design", "Furniture", "Lighting", "Fixture", "Lamp", "Chandelier", "Sconce", "Table", "Chair", "Sofa", "Bed", "Mattress", "Pillow", "Blanket", "Rug", "Carpet", "Flooring", "Tile", "Wallpaper", "Paint", "Brush", "Canvas", "Easel", "Artwork", "Painting", "Drawing", "Sketch", "Print", "Poster", "Photography", "Camera", "Lens", "Tripod", "Film", "Video", "Animation", "Graphics", "Illustration", "Comic", "Cartoon", "Manga", "Book", "Novel", "Poetry", "Literature", "Magazine", "Newspaper", "Journal", "Blog", "Website", "Social media", "Technology", "Innovation", "Science", "Mathematics", "Education", "Learning", "Research", "Development", "Industry", "Manufacturing", "Production", "Transportation", "Logistics", "Service", "Hospitality", "Tourism", "Recreation", "Sports", "Fitness", "Health", "Wellness", "Beauty", "Cosmetics", "Personal care", "Nutrition", "Diet", "Cooking", "Food", "Beverage", "Restaurant", "Cafe", "Bar", "Pub", "Wine", "Beer", "Spirits", "baby", "infant", "newborn", "toddler", "nursery", "diaper", "pacifier", "bottle", "formula", "breastfeeding", "stroller", "crib", "blanket", "swaddle", "onesie", "bib", "burp cloth", "rattle", "teether", "mobile", "baby monitor", "playpen", "high chair", "car seat", "baby carrier", "baby food", "baby shampoo", "baby lotion", "baby powder", "baby oil", "baby wipes", "baby bath", "baby massage", "baby clothes", "baby shoes", "baby toys", "baby books", "baby development", "baby health", "baby sleep", "baby safety", "parenting", "motherhood", "fatherhood", "family", "child", "children", "kids", "babysitting", "childcare", "nanny", "playdate", "maternity", "paternity", "baby announcement", "baby shower", "baby naming", "baby milestones", "baby photography", "baby fashion", "baby gear", "baby proofing", "baby registry", "baby sign language", "baby sign", "babywearing", "baby wearing", "tummy time", "baby-friendly", "baby-led weaning", "breast pump", "bassinet", "baby bassinet", "baby bouncer", "baby swing", "baby jumper", "baby gym", "baby playmat", "baby teething", "baby fever", "baby illness", "baby vaccination", "baby medicine", "baby first aid", "baby CPR", "baby safety gate", "baby gate", "baby monitor camera", "baby video monitor", "baby audio monitor", "baby night light", "baby white noise", "baby sleep aid", "baby sleep training", "baby schedule", "baby routine", "baby massage oil", "baby colic", "baby reflux", "baby eczema", "baby acne", "baby skin care", "baby laundry detergent", "baby travel", "baby car mirror", "baby car mirror for rear facing", "baby thermometer", "baby nasal aspirator", "baby humidifier", "baby decongestant", "baby saline drops", "baby sunscreen", "baby swimwear", "baby pool", "baby swim lessons", "baby swim safety", "baby float", "baby life jacket", "baby beach gear", "baby carrier wrap", "baby carrier sling", "baby carrier backpack", "baby carrier front facing", "baby carrier facing out", "baby carrier hip", "baby carrier newborn", "baby carrier 360", "baby carrier ergo", "baby carrier lillebaby", "baby carrier tula", "baby carrier infantino", "baby carrier moby", "baby carrier mei tai", "baby carrier ring sling"]

    for sub_folder in sub_folders:
        region = 0
        folder_name = os.path.join(main_folder)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        driver.get("https://www.google.com/imghp")
        search_bar = driver.find_element(By.NAME, "q")
        search_bar.send_keys(query + " " + sub_folder)
        search_bar.submit()

        # Wait for the page to load
        time.sleep(3)

        # Scroll to the bottom of the page multiple times
        for i in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # Download the first 100 images
        imgs = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
        # pdb.set_trace()
        print(f"Found {len(imgs)} images for query '{query}' and region '{sub_folder}'")
        
        for i, img in enumerate(imgs[:500]):
            try:
                src = img.get_attribute("src")
                alt = img.get_attribute("alt")
                height = int(img.get_attribute("height"))
                width = int(img.get_attribute("width"))
                if not (height > 24 and width > 24):
                    continue
                
                for word in not_related_to_baby:
                    if word.lower() in alt.lower():
                        continue 
                urllib.request.urlretrieve(src, f"{folder_name}/{total+1}_{alt}.jpg")
                print(f"[{total+1} of {target}] Downloaded image {region+1} of 100 for query '{query}' and region '{sub_folder}'")
                total += 1
                region += 1
                if region == 100 or total == target:
                    break
            except:
                print(f"Error downloading image {i+1} of 100 for query '{query}' and region '{sub_folder}'")
                pass
        
        if total == target:
            break
# Close the browser
driver.quit()
