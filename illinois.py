import requests
import pandas as pd
from datetime import date
from datetime import datetime


def main():
    df = pd.DataFrame(
        columns=['district', 'city', 'county', 'instructional delivery', 'school count', 'grades served', 'total PreK-12 enrollment',
                 'modified id', 'date scraped'])
    url = "https://services2.arcgis.com/3yCQWqEMIRwEdrth/arcgis/rest/services/School_District_Survey_Public/FeatureServer/0/query?f=json&where=(InstrFormat%20%3D%20%27Blended%20Remote%20Learning%27)%20OR%20(InstrFormat%20%3D%20%27In-Person%20Learning%27)%20OR%20(InstrFormat%20%3D%20%27Remote%20Learning%27)&returnGeometry=false&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=USER_Facil%20asc&resultOffset=0&resultRecordCount=670&resultType=standard&cacheHint=true"
    openUrl = requests.get(url)
    jsonD = openUrl.json()
    print("IL - Downloaded JSON")
    for p in jsonD["features"]:
        district = p["attributes"]["USER_Facil"]
        city = p["attributes"]["USER_City"]
        county = p["attributes"]["USER_Count"]
        instructional_delivery = p["attributes"]["InstrFormat"]
        school_count = p["attributes"]["School_Count"]
        grades_served = p["attributes"]["GradeServed"]
        total_enrollment = p["attributes"]["PreK_12_Total_Enrollment"]
        modified_id = p["attributes"]["Modified"]
        new_row = pd.Series(data={'district': district, 'city': city, 'county': county,
                                  'instructional delivery': instructional_delivery, 'school count': school_count,
                                  'grades served': grades_served, 'total PreK-12 enrollment': total_enrollment,
                                  'modified id': modified_id, 'date scraped': date.today()})
        df = df.append(new_row, ignore_index=True)
    df.to_csv('out/Illinois' + datetime.now().strftime('%m-%d-%Y') + '.csv', index=False)
    print("IL - Wrote CSV")

#main()
