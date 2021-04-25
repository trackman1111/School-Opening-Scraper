import logging

import requests
from datetime import datetime

def main():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    download_xslx()
    #print("WA - Downloaded CSV")

def download_xslx():
    # CSV API URL
    # use limit=50000 to force maximum record amount
    dataUrl = "https://data.wa.gov/resource/9i5d-c2m8.csv?$limit=50000&$offset=0"
    # Retrieve CSV file in pages (max 50000 records/page)
    file = requests.get(dataUrl)
    logging.info("Received Washington Data", exc_info=False);
    csvPath = "out/WA_" + datetime.now().strftime('%Y%m%d') + ".csv"
    open(csvPath, 'wb').write(file.content)
    logging.info("Wrote Washington Data", exc_info=False);

#main()
