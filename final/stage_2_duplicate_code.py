class URLS:
    def __init__(self):
        self.local_recovered = "C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Recovered.xlsx"
        self.local_deaths = "C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Deaths.xlsx"
        self.local_confirmed = "C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Confirmed.xlsx"
        self.local_countries = "C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Countries.xlsx"

        self.global_time_series_recovered = "https://github.com/CSSEGISandData/COVID-19/blob/master/" \
                                            "csse_covid_19_data/csse_covid_19_time_series/" \
                                            "time_series_covid19_recovered_global.csv"
        self.global_time_series_deaths = "https://github.com/CSSEGISandData/COVID-19/blob/master/" \
                                         "csse_covid_19_data/csse_covid_19_time_series/" \
                                         "time_series_covid19_deaths_global.csv"
        self.global_time_series_confirmed = "https://github.com/CSSEGISandData/COVID-19/blob/master/" \
                                            "csse_covid_19_data/csse_covid_19_time_series/" \
                                            "time_series_covid19_confirmed_global.csv"
        self.global_time_series_countries = "https://www.worldometers.info/coronavirus"


def update_local_file(local_file, url):
    workbook = xlsxwriter.Workbook(local_file)
    workbook.close()
    response = requests.get(url)
    html = response.content
    soup = bs4.BeautifulSoup(html, "lxml")
    tables = soup.findAll("table")
    wb = op.load_workbook(local_file)
    ws = wb.get_sheet_by_name("Sheet1")
    table = tables[0]
    for row in table.findAll('tr')[1:]:
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        ws.append(list_of_cells)
    wb.save(filename=local_file)
    wb.close()


def refresh():
    urls = URLS()
    os.remove()
    update_local_file(urls.local_recovered, urls.global_time_series_recovered)
    update_local_file(urls.local_deaths, urls.global_time_series_deaths)
    update_local_file(urls.local_confirmed, urls.global_time_series_confirmed)
    update_local_file(urls.local_countries, urls.global_time_series_countries)
