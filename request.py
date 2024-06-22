import requests 
from datetime import datetime

""" from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display
import chromedriver_autoinstaller """


current_time_and_date = datetime.now().strftime('%Y-%m-%d_%H-%M')

yyc_json_data = requests.get('https://rmsflightdata.yyc.com:8091/flights')


yyc_filename = 'data/yyc_flight_data_' + str(current_time_and_date) + '.json'

file = open(yyc_filename, 'w')
file.write(yyc_json_data.text)
file.close()



yyz_arrivals_json_data = requests.get('https://gtaa-fl-prod.azureedge.net/api/flights/list?type=ARR&day=today&useScheduleTimeOnly=false')

yyz_arrivals_filename = 'data/yyz/arrivals/yyz_flight_data_' + str(current_time_and_date) + '.json'

file = open(yyz_arrivals_filename, 'w')
file.write(yyz_arrivals_json_data.text)
file.close()



yyz_departures_json_data = requests.get('https://gtaa-fl-prod.azureedge.net/api/flights/list?type=DEP&day=today&useScheduleTimeOnly=false')

yyz_departures_filename = 'data/yyz/departures/yyz_flight_data_' + str(current_time_and_date) + '.json'

file = open(yyz_departures_filename, 'w')
file.write(yyz_departures_json_data.text)
file.close()


""" chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.yvr.ca/_api/Flights")
yvr_text = driver.find_elements(By.TAG_NAME, "body")[0]

yvr_filename = 'data/yvr/yvr_flight_data_' + str(current_time_and_date) + '.json'

file = open(yvr_filename, 'w')
file.write(yvr_text.text)
file.close()

driver.quit() """