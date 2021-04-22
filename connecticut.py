import pandas as pd
from datetime import date
from datetime import datetime
import requests


def main():
    df = pd.DataFrame(
        columns=["district code", "district name", "in-person grades", "hybrid grades", "remote grades",
                 "predominant learning model", "organization type", "alliance district",
                 "reporting period", "date updated", "date scraped"])
    api_url = "https://data.ct.gov/resource/5q7h-u2ac.json"
    response = requests.get(api_url)
    data = response.json()
    # print("CT - Got JSON Data")

    for properties in data:
        districtCode = properties["district_code"]
        districtName = properties["district_name"]
        inPerson = properties["grades_inperson_model"]
        hybrid = properties["grades_hybrid_model"]
        remote = properties["grades_remote_model"]
        predom = properties["predominant_model"]
        orgType = properties["organization_type"]
        try:
            alliance = properties["alliance_district"]
        except:
            alliance = ""
        reportPeriod = properties["reporting_period"]
        dateUpdate = properties["update_date"]

        new_row = pd.Series(
            data={"district code": districtCode, "district name": districtName, "in-person grades": inPerson,
                  "hybrid grades": hybrid, "remote grades": remote, "predominant learning model": predom,
                  "organization type": orgType, "alliance district": alliance,
                  "reporting period": reportPeriod, "date updated": dateUpdate, "date scraped": date.today()})
        df = df.append(new_row, ignore_index=True)

    df.to_csv('out/CT_' + datetime.now().strftime('%Y%m%d') + '.csv', index=False)
    #print("CT - Wrote CSV")

main()
