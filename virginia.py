from tableauscraper import TableauScraper as TS
from datetime import datetime

def main():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    url="https://public.tableau.com/views/R2L2020/Division"

    ts = TS()
    ts.loads(url)
    workbook = ts.getWorkbook()
    logging.info("Received Virginia Data", exc_info=False);

    for t in workbook.worksheets:
        df = t.data
    df.to_csv("VA_" + datetime.now().strftime('%Y%m%d'))
    logging.info("Wrote Virginia Data", exc_info=False);

main()
