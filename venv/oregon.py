import requests
import urllib
import csv
from openpyxl import load_workbook
from bs4 import BeautifulSoup

def main():
    download_xslx()
    copy_to_new_csv()

def download_xslx():
    # Get html of page
    url = "https://www.oregon.gov/ode/students-and-family/healthsafety/Pages/2020-21-School-Status.aspx"
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Get the most recent update link
    path = soup.body.main.div.contents[9].li.a['href']
    dataUrl = "https://www.oregon.gov/" + path

    # Retrieve cvs file
    urllib.request.urlretrieve(dataUrl, './OregonOriginal.xlsx')
    print("Downloaded OR xlsx")
    
def copy_to_new_csv():
    wb = load_workbook('OregonOriginal.xlsx')
    districtSheet = wb['District List']
    for row in districtSheet.iter_rows(values_only=True):
        print(row)

main()