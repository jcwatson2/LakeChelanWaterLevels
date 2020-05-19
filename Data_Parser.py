import csv
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By

from Data_Entry import Data_Entry

class Data_Parser:
    def __init__(self, start_date, current_date):
        self.date_list = list()
        self.entry_list = list()
        self.start_date = start_date
        self.current_date = current_date

    def parse(self):
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        driver = webdriver.Chrome(options=op)
        driver.get("https://waterdata.usgs.gov/nwis/uv?cb_00062=on&format=rdb&site_no=12452000&period=&"
                   "begin_date=" + self.start_date + "&end_date=" + self.current_date)

        data = driver.find_element(By.XPATH, '/html/body/pre').text
        data_file = open("data_file.csv", "w")
        for line in data.splitlines():
            if not line.startswith('#'):
                data_file.write(line + "\n")
        driver.quit()
        data_file = open("data_file.csv", "r")
        parser = csv.reader(data_file, delimiter=' ')
        parser.__next__()
        parser.__next__()
        for row in parser:
            entry = Data_Entry(row[3], row[5])
            self.date_list.append(row[2])
            self.entry_list.append(entry)

        data_file.close()


