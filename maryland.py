from datetime import date

import requests
import pandas as pd

def main():
    download_csv()

def download_csv():
    df = pd.DataFrame(
        columns=["objectID", "school", "county report", "number of total cases", "report date", "date scraped"])
    api_url = "https://opendata.arcgis.com/datasets/004454e8b70847f89b776b1caf94b30b_0.geojson"
    response = requests.get(api_url)
    print(response.status_code)
    data = response.json()

    for p in data["features"]:
        properties = p["properties"]
        object_id = properties["OBJECTID"]
        school = properties["School"]
        county_report = properties["CountyReport"]
        num_cases = properties["Number_of_Total_Cases"]
        report_date = properties["ReportDate"]
        new_row = pd.Series(data={"objectID": object_id, "school": school, "county report": county_report,
                                  "number of total cases": num_cases, "report date": report_date,
                                  "date scraped": date.today()})
        df = df.append(new_row, ignore_index=True)

    df.to_csv('Maryland'+ str(date.today()) + '.csv', index=False)

main()