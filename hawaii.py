from tableauscraper import TableauScraper as TS
from datetime import datetime

def main():
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

    url="https://public.tableau.com/views/COVIDPlanningTool-Embed700px/SimpleDashboard?:embed=y&amp;:showVizHome=no&amp;:host_url=https%3A%2F%2Fpublic.tableau.com%2F&amp;:embed_code_version=3&amp;:tabs=no&amp;:toolbar=yes&amp;:animate_transition=yes&amp;:display_static_image=no&amp;:display_spinner=no&amp;:display_overlay=yes&amp;:display_count=yes&amp;:language=en&amp;publish=yes&amp;:loadOrderID=0"
    ts = TS()
    ts.loads(url)
    logging.info("Received Hawaii Data", exc_info=False);

    ws = ts.getWorksheet("CDC Map")
    ws.data.to_csv("HI_" + datetime.now().strftime('%Y%m%d') + ".csv")
    logging.info("Wrote Hawaii Data", exc_info=False);

main()
