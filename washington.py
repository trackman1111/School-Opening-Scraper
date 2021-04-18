import requests
from datetime import datetime

def main():
    download_xslx()
    print("WA - Downloaded CSV")

def download_xslx():
    # CSV API URL
    # use limit=50000 to force maximum record amount
    dataUrl = "https://data.wa.gov/resource/9i5d-c2m8.csv?$limit=50000&$offset=0"

    # Retrieve CSV file in pages (max 50000 records/page)
    file = requests.get(dataUrl)
    csvPath = "out/Washington" + datetime.now().strftime('%m-%d-%Y') + ".csv"
    open(csvPath, 'wb').write(file.content)

#main()
