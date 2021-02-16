from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

WHATSAPP = 'http://web.whatsapp.com'
PROFILE_PATH = 'C:/Users/pbohr/AppData/Roaming/Mozilla/Firefox/Profiles/rvqzov3w.AutoMate'

# WhatsApp needs to be logged in
options = Options()
options.profile = PROFILE_PATH

service = Service('geckodriver')

driver = webdriver.Firefox(options=options, service=service)
driver.get(WHATSAPP)

# Wait for whatsapp to load in our initiating element
WebDriverWait(driver, 10).until(
    EC.all_of(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[title='VMC OIC-2 batch 2022'")),
        EC.none_of(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#startup")),
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#initial-startup"))
        )
    )
)

# Get to the actual gruop
group_name_span = driver.find_element(By.CSS_SELECTOR,"span[title='VMC OIC-2 batch 2022'")
location = group_name_span.location
action = ActionChains(driver)
action.move_to_element(group_name_span).click().perform()

# Get all the messages
messages = driver.find_elements((By.CLASS_NAME, 'message-in'))

# TODO:
# Use XPaths to get to the class and id-less <span> tag with the main text
# Feed it into a regex and pick off the link
# If a valid link is found get the time
# Sort by time 

input()
driver.quit()
