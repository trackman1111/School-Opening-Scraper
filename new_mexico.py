import tabula
from pathlib import Path
import os
import requests
import csv
from bs4 import BeautifulSoup
from datetime import date


def main():
    write_csv()


def write_csv():
    url = "https://webnew.ped.state.nm.us/"
    page = requests.get(url)

    url = 'toNMSDP'
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, 'html5lib')

        linkcol = soup.find(class_="col-md-4")
        for linktxt in linkcol.find_all("a", href=True):
            if linktxt.contents[0] == 'School Reentry Status':
                #print('NM - Link Found')
                url = linktxt.get('href')
    else:
        print("NM - page request error with ", page.status_code)

    pdfPathName = 'temp/New_Mexico_SDP.pdf'
    today = date.today()
    finalCSVpath = 'out/New_Mexico_' + today.strftime("%m-%d-%y") + '.csv'
    filename = Path(pdfPathName)
    response = requests.get(url)
    filename.write_bytes(response.content)

    #print('NM - Got PDF')

    # Silent mode to disable ApachePDF font errors that don't affect output
    tabula.convert_into(pdfPathName, finalCSVpath, output_format="csv", pages='all', silent=True)

    #print('NM - Converted to CSV')

    lines = list()
    csvhead = ['School district', 'School name', 'Reopening Policy', 'County']
    lines.append(csvhead)
    with open(finalCSVpath, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            # print(row)
            if row[0] != "DISTRICT" and row[0] != "":
                lines.append(row)
        #print('NM - Opened CSV')

    with open(finalCSVpath, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
        #print('NM - Reformatted CSV')

    try:
        os.remove(pdfPathName)
        #print('NM - Deleted PDF')
    except:
        print("NM - Could not delete file")

#main()