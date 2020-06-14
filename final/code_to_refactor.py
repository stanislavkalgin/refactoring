        def refresh():
            os.remove()
            workbook = xlsxwriter.Workbook("C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Recovered.xlsx")
            workbook.close()
            url = "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
            response = requests.get(url)
            html = response.content
            soup = bs4.BeautifulSoup(html, "lxml")
            tables = soup.findAll("table")
            wb = op.load_workbook("C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Recovered.xlsx")
            ws = wb.get_sheet_by_name("Sheet1")
            table = tables[0]
            for row in table.findAll('tr')[1:]:
                list_of_cells = []
                for cell in row.findAll('td'):
                    text = cell.text.replace('&nbsp;', '')
                    list_of_cells.append(text)
                ws.append(list_of_cells)
            wb.save(filename='C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Recovered.xlsx')
            wb.close()
            workbook = xlsxwriter.Workbook(
                "C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Deaths.xlsx")
            workbook.close()
            url = "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
            response = requests.get(url)
            html = response.content
            soup = bs4.BeautifulSoup(html, "lxml")
            tables = soup.findAll("table")
            wb = op.load_workbook("C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Deaths.xlsx")
            ws = wb.get_sheet_by_name("Sheet1")
            table = tables[0]
            for row in table.findAll('tr')[1:]:
                list_of_cells = []
                for cell in row.findAll('td'):
                    text = cell.text.replace('&nbsp;', '')
                    list_of_cells.append(text)
                ws.append(list_of_cells)
            wb.save(filename='C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Deaths.xlsx')
            wb.close()
            workbook = xlsxwriter.Workbook(
				"C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Confirmed.xlsx")
            workbook.close()
            url = "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
            response = requests.get(url)
            html = response.content
            soup = bs4.BeautifulSoup(html, "lxml")
            tables = soup.findAll("table")
            wb = op.load_workbook("C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Confirmed.xlsx")
            ws = wb.get_sheet_by_name("Sheet1")
            table = tables[0]
            for row in table.findAll('tr')[1:]:
                list_of_cells = []
                for cell in row.findAll('td'):
                    text = cell.text.replace('&nbsp;', '')
                    list_of_cells.append(text)
                ws.append(list_of_cells)
            wb.save(filename='C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Confirmed.xlsx')
            wb.close()
            workbook = xlsxwriter.Workbook(
                "C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Countries.xlsx")
            workbook.close()
            url = "https://www.worldometers.info/coronavirus"
            response = requests.get(url)
            html = response.content
            soup = bs4.BeautifulSoup(html, "lxml")
            tables = soup.findAll("table")
            wb = op.load_workbook("C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Countries.xlsx")
            ws = wb.get_sheet_by_name("Sheet1")
            table = tables[0]
            for row in table.findAll('tr')[1:]:
                list_of_cells = []
                for cell in row.findAll('td'):
                    text = cell.text.replace('&nbsp;', '')
                    text = cell.text.replace(',', '')
                    list_of_cells.append(text)
                ws.append(list_of_cells)
            wb.save(filename='C:/Users/yasharth dubey/Documents/Python Scripts/COVID19 management/Countries.xlsx')
            wb.close()
