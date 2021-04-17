import pandas as pd
from datetime import date
from datetime import datetime
import requests


def main():
    df = pd.DataFrame(
        columns=["district", "facilityid", "facilityname", "city", "school_total", "reporting_period", "dateupdated"])
    api_url = "https://data.ct.gov/resource/u8jq-fxc2.json"
    response = requests.get(api_url)
    data = response.json()

    for properties in data:
        district = properties["district"]
        school_id = properties["facilityid"]
        school = properties["facilityname"]
        city = properties["city"]
        num_cases = properties["school_total"]
        report_date = properties["reporting_period"]
        new_row = pd.Series(data={"district": district, "facilityid": school_id, "facilityname": school, "city": city,
                                  "school_total": num_cases, "reporting_period": report_date,
                                  "dateupdated": date.today()})
        df = df.append(new_row, ignore_index=True)

    df.to_csv('Connecticut' + datetime.now().strftime('%m-%d-%Y') + '.csv', index=False)
main()
