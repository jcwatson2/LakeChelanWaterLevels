from datetime import date

from selenium import webdriver

driver = webdriver.Chrome()
startdate = input("Start date: ")
currentdate = str(date.today())
print(currentdate)
driver.get("https://waterdata.usgs.gov/nwis/uv?cb_00062=on&format=rdb&site_no=12452000&period=&"
           "begin_date="+startdate+"&end_date="+currentdate)


