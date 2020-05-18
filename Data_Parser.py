import csv
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By

from Data_Entry import Data_Entry

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
startdate = input("Start date: ")
currentdate = str(date.today())
print(currentdate)
driver.get("https://waterdata.usgs.gov/nwis/uv?cb_00062=on&format=rdb&site_no=12452000&period=&"
           "begin_date="+startdate+"&end_date="+currentdate)

data = driver.find_element(By.XPATH, '/html/body/pre').text
level_data = dict()
data_file = open("data_file.csv", "w")
for line in data.splitlines():
    if not line.startswith('#'):
        data_file.write(line + "\n")
data_file = open("data_file.csv", "r")
parser = csv.reader(data_file, delimiter=' ')
parser.__next__()
parser.__next__()
date_list = list()
entry_list = list()
for row in parser:
    entry = Data_Entry(row[3], row[5])
    date_list.append(row[2])
    entry_list.append(entry)

data_file.close()

driver.quit()

