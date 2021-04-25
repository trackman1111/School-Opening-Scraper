import logging

import requests
from csv import reader
import pandas as pd
from datetime import date
from datetime import datetime


def main():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    download_csv()
    logging.info("Received Rhode Island Data", exc_info=False);
    copy_to_new_csv()
    logging.info("Wrote Rhode Island Data", exc_info=False);


def download_csv():
    url = "https://docs.google.com/spreadsheet/ccc?key=1c2QrNMz8pIbYEKzMJL7Uh2dtThOJa2j1sSMwiDo5Gz4&gid=594871904&output=csv"
    # Retrieve cvs file
    originalFile = requests.get(url)
    open('temp/RIOriginal.csv', 'wb').write(originalFile.content)


def copy_to_new_csv():
    originalFile = open('temp/RIOriginal.csv', 'r', newline='', encoding='utf-8')
    csvReader = reader(originalFile, delimiter=',')
    inputRow = 0
    df = pd.DataFrame(
        columns=['school', 'district', 'model', 'new student cases in past 7 days',
                 'cumulative student cases since 9/14/2020', 'new staff cases in past 7 days',
                 'cumulative staff cases since 9/14/2020', 'date updated',
                 'cases updated', 'date scraped'])

    for row in csvReader:
        # Row contains general info:
        if inputRow == 0 or inputRow == 2 or inputRow == 3:
            inputRow += 1
            continue

        # Row contains dates updated:
        if inputRow == 1:  # Get date updated
            dateUpdated = str(row[0])[18:27]
            casesUpdated = str(row[0])[61:70]
            inputRow += 1
            continue

        # Reached data sources at end of file
        if "Data Sources" in row[0]:
            break

        # Row is a section header:
        if "In-Person and Hybrid Cases" in row[0]:
            model = "In-Person and Hybrid"
            inputRow += 1
            continue
        elif "Virtual Cases" in row[0]:
            model = "Virtual"
            inputRow += 1
            continue

        # Row contains totals
        if row[0] == "":
            inputRow += 1
            continue

        if not model:
            model = ""
            print("RI - Error getting instruction model")

        # Row is a school:
        school = row[0]
        district = row[1]
        cases1 = row[2]
        cases2 = row[3]
        cases3 = row[4]
        cases4 = row[5]

        newRow = pd.Series(data={'school': school, 'district': district, 'model': model,
                                 'new student cases in past 7 days': cases1,
                                 'cumulative student cases since 9/14/2020': cases2,
                                 'new staff cases in past 7 days': cases3,
                                 'cumulative staff cases since 9/14/2020': cases4,
                                 'date updated': dateUpdated, 'cases updated': casesUpdated,
                                 'date scraped': date.today()})

        df = df.append(newRow, ignore_index=True)

        inputRow += 1  # End for
    originalFile.close()
    df.to_csv('out/RI_' + datetime.now().strftime('%Y%m%d') + '.csv', index=False)  # Copy dataframe to CSV


#main()
