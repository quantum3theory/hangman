from selenium import webdriver
import urllib.request
import time
# Let's define our class
class AnimalScraper:
    def __init__(self, animal, homepage):
        self.animal = animal
        self.homepage = homepage
        self.driver = webdriver.Chrome()
        #self.links = [] # Initialise links, so that if the user calls for get_image_source, it does not throw an error.
    
    def extract_links(self) -> None:
        self.driver.get(self.homepage + self.animal)
        animal_list = self.driver.find_elements_by_xpath('//figure[@itemprop="image"]')
        self.links = []
        for item in animal_list:
            self.links.append(item.find_element_by_xpath('.//a').get_attribute('href'))
        return self.links

    def get_image_source(self, link: str) -> None:
        self.driver.get(link)
        time.sleep(0.5)
        self.src = self.driver.find_element_by_xpath('//img[@class="oCCRx"]').get_attribute('src')

    def download_images(self, i) -> None:
        urllib.request.urlretrieve(self.src, f"./animals/{self.animal}_{i}.jpg")
    
    def get_animal_images(self):
        all_links = self.extract_links()
        for i, link in enumerate(all_links):
            self.get_image_source(link)
            self.download_images(i)
        self.links = []
        
cat_scraper = AnimalScraper('cat', 'https://unsplash.com/t/animals')