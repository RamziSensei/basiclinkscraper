from selenium import webdriver
import csv


driver = webdriver.Chrome(r"C:/Users/ramzi/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe")
driver.get("https://edix2018.tems-system.com/eguide/eng/list")

links = driver.find_elements_by_xpath('//*[@id="exhibitor_expo"]/ul/li[1]/a')


with open('techList.csv','a') as csvFile:
    writer = csv.writer(csvFile)
    for i in range(1,450):
        for link in links:
            writer.writerow([link.text,link.get_attribute('href')])
            #print(link.text)
            #print(link.get_attribute('href'))
        links = driver.find_elements_by_xpath('//*[@id="exhibitor_expo"]/ul/li['+str(i)+']/a')

