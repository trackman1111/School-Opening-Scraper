import requests
from csv import reader
import pandas as pd
from datetime import date
from datetime import datetime


def main():
    download_csv()
    #print("NC - Downloaded CSV")
    copy_to_new_csv()
    #print("NC - Wrote CSV")

# Instruction Plan Definitions: https://covid19.ncdhhs.gov/media/164/open

def download_csv():
    url = "https://docs.google.com/spreadsheet/ccc?key=1We8gDpa4Do5NR83Nf8niGE_YxzLDf-KZh-tVWifStxE&output=csv"
    # Retrieve cvs file
    originalFile = requests.get(url)
    open('temp/NCOriginal.csv', 'wb').write(originalFile.content)


def copy_to_new_csv():
    originalFile = open('temp/NCOriginal.csv', 'r', newline='', encoding='utf-8')
    csvReader = reader(originalFile, delimiter=',')
    inputRow = 0
    df = pd.DataFrame(
        columns=['district', '2019-2020 average daily membership', '2020-2021 average daily membership',
                 'plan a (in-person)', 'plan b (hybrid)', 'plan c (remote)', 'virtual option', 'date scraped'])

    for row in csvReader:
        if inputRow == 0 or inputRow == 1:  # Skip column headers
            inputRow += 1
            continue
        districtName = row[0]
        adm1920 = row[1]
        adm2021 = row[2]
        planA = row[3]
        planB = row[4]
        planC = row[5]
        virtual = row[6]
        if districtName is None:  # End of input file
            break

        newRow = pd.Series(data={'district': districtName, '2019-2020 average daily membership': adm1920,
                                 '2020-2021 average daily membership': adm2021, 'plan a (in-person)': planA,
                                 'plan b (hybrid)': planB, 'plan c (remote)': planC, 'virtual option': virtual,
                                 'date scraped': date.today()})

        df = df.append(newRow, ignore_index=True)

        inputRow += 1  # End for
    originalFile.close()
    df.to_csv('out/NC_' + datetime.now().strftime('%Y%m%d') + '.csv', index=False)  # Copy dataframe to CSV

#main()
