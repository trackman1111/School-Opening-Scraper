import requests
import urllib
import csv
from csv import reader


def main():
    print("test")
    #download_csv()
    #copy_to_new_csv()

def download_csv():
    url = "https://public.tableau.com/vizql/w/R2L2020/v/R2L/tempfile/sessions/53FC07EE12434A21990049852B616107-0:0/?key=1430079797&keepfile=yes&attachment=yes"
    urllib.request.urlretrieve(url, 'temp/VirginiaOriginal.csv')
    print("Downloaded VA csv")


def copy_to_new_csv():
    f1 = open('temp/VirginiaOriginal.csv', 'r', newline='', encoding='utf-16')
    f2 = open('out/SchoolDistricts.csv', 'a')
    csv_reader = reader(f1, delimiter='\t')
    csv_writer = csv.writer(f2)
    i = 0;
    date_update = "none"
    for row in csv_reader:
        if i == 1:
            date_update = row[len(row)-1]
        if (row[len(row)-1] != "") and (i > 1):
            csv_writer.writerow(["Virginia", row[1],row[len(row)-1], date_update])
        i += 1
    f1.close()
    f2.close()


main()
