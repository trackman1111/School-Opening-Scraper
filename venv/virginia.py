import requests
import urllib
import csv
from csv import reader


def main():
    download_csv()
    copy_to_new_csv()



def download_csv():
    url = "https://public.tableau.com/vizql/w/R2L2020/v/Division/tempfile/sessions/785D6C7052744A7B801670EAFCA6F501-0:0/?key=3351444022&keepfile=yes&attachment=yes "
    urllib.request.urlretrieve(url, './VirginiaOriginal.csv')
    print("Downloaded VA csv")


def copy_to_new_csv():
    f1 = open("VirginiaOriginal.csv", 'r', newline='', encoding='utf-16')
    f2 = open('Complete.csv', 'a')
    csv_reader = reader(f1, delimiter='\t')
    csv_writer = csv.writer(f2)
    for row in csv_reader:
        csv_writer.writerow(["Virginia", row[1],row[len(row)-1]])



def organize_data():
    print("Organized")
