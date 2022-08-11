import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup as BS


def get_response(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return 'Error'


def get_data(html):
    current_data = datetime.now().strftime('%m_%d_%Y')
    soup = BS(html, 'lxml')
    table = soup.find('table')
    thead = table.find_all('tr')
    links = table.find_all('a')
   

    table_headers = []
    table_cities = [[]]
    

    for i in thead:
        table_th = i.find_all('th')
        table_td = i.find_all('td')
        if table_th:
            for th in table_th:
                th = th.text.strip()
                table_headers.append(th)
              
        if table_td:
            cities = []
            for td in table_td:
                td = td.text.strip()
                cities.append(td)

            table_cities.append(cities)

            
    for link in links:
        table_link = link
        if table_link.has_attr('href'):
            table_href = {}
        # table_link = link.find_all('a')
            table_href.append(link.get('href'))
        table_cities.append(table_href)


    with open(file=f'data_{current_data}.csv', mode='w', encoding='UTF-8') as file:
        writer = csv.writer(file)

        writer.writerow(table_headers)

        for row in table_cities:
            writer.writerow(row)

    return table_headers

def main():
    URL = 'https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0_%D0%9A%D0%B8%D1%80%D0%B3%D0%B8%D0%B7%D0%B8%D0%B8'
    html = get_response(url=URL)
    # print(html)

    table = get_data(html)
    print(table)

# if name == '__main__':#
main()
