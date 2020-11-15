import requests
from bs4 import BeautifulSoup
from xlwt import Workbook
from multiprocessing import Process, Queue
from multiprocessing import Pool
import logging
import multiprocessing
row = 0
col = 0
wb = Workbook()
counter = 0
sheet1 = wb.add_sheet('Sheet 1')


def get_html(url):
    try:
        r = requests.get(url)
        return r.text
    except Exception as error:
        print(error)


def get_total_pages(html):
    return 5
    # soup = BeautifulSoup(html, 'lxml')

    # pages = soup.find('div', class_='pager').find_all('a', class_='')[-1].text

    # return int(pages)


def get_page_data(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        pages = soup.find_all('a', class_='ddl_product_link')
        pages = list(dict.fromkeys(pages))
        for i in pages:
            try:
                kv = i.get('href')
                kv_html = get_html('https://kolesa.kz' + kv)
                print('https://kolesa.kz' + kv)
                p = Process(target=get_kv_info(kv_html),)
                p.start()
            except Exception as error:
                print(error)
    except Exception as error:
        print(error)


def get_kv_info(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        try:
            offer__parameters = soup.find(
                'div', class_='offer__parameters').find_all('dl')
        except:
            offer__parameters = "None"
        try:
            offer__title = soup.find(
                'h1', class_='offer__title').find_all('span')
        except:
            offer__title = "None"
        try:
            shell = ''
            for dt in offer__parameters:
                if (dt.find(title='Кузов')):
                    shell = dt.find(title='Кузов').parent.find(
                        'dd').text.strip()
        except:
            shell = "None"
        try:
            cost = soup.find('div', class_='offer__price').text.strip()
        except:
            cost = "None"
        try:
            location = ''
            for dt in offer__parameters:
                if (dt.find(title='Город')):
                    location = dt.find(title='Город').parent.find(
                        'dd').text.strip()
        except:
            location = ""
        try:
            engineVolume = ''
            for dt in offer__parameters:
                if (dt.find(title='Объем двигателя, л')):
                    engineVolume = dt.find(
                        title='Объем двигателя, л').parent.find('dd').text.strip()
        except:
            engineVolume = ""
        try:
            mileage = ''
            for dt in offer__parameters:
                if (dt.find(title='Пробег')):
                    mileage = dt.find(title='Пробег').parent.find(
                        'dd').text.strip()
        except:
            mileage = ""
        try:
            transmission = ''
            for dt in offer__parameters:
                if (dt.find(title='Коробка передач')):
                    transmission = dt.find(
                        title='Коробка передач').parent.find('dd').text.strip()
        except:
            transmission = "None"
        try:
            rudder = ''
            for dt in offer__parameters:
                if (dt.find(title='Руль')):
                    rudder = dt.find(title='Руль').parent.find(
                        'dd').text.strip()
        except:
            rudder = "None"
        try:
            color = ''
            for dt in offer__parameters:
                if (dt.find(title='Цвет')):
                    color = dt.find(title='Цвет').parent.find(
                        'dd').text.strip()
        except:
            color = "None"
        try:
            gear = ''
            for dt in offer__parameters:
                if (dt.find(title='Привод')):
                    gear = dt.find(title='Привод').parent.find(
                        'dd').text.strip()
        except:
            gear = "None"
        try:
            customCleared = ''
            for dt in offer__parameters:
                if (dt.find(title='Растаможен в Казахстане')):
                    customCleared = dt.find(
                        title='Растаможен в Казахстане').parent.find('dd').text.strip()
        except:
            customCleared = "None"

        global col
        global row
        global counter
        global sheet1
        sheet1.write(row, col, row)
        col = col + 1
        sheet1.write(row, col, location)
        col = col + 1
        sheet1.write(row, col, offer__title[0].text + offer__title[1].text)
        col = col + 1
        sheet1.write(row, col, offer__title[2].text)
        col = col + 1
        sheet1.write(row, col, shell)
        col = col + 1
        sheet1.write(row, col, engineVolume)
        col = col + 1
        sheet1.write(row, col, mileage)
        col = col + 1
        sheet1.write(row, col, transmission)
        col = col + 1
        sheet1.write(row, col, rudder)
        col = col + 1
        sheet1.write(row, col, color)
        col = col + 1
        sheet1.write(row, col, gear)
        col = col + 1
        sheet1.write(row, col, customCleared)
        col = col + 1
        sheet1.write(row, col, cost)
        col = col + 1
        row = row + 1
        col = 0
        counter = counter + 1
        wb.save('./result/result.xls')
    except Exception as error:
        print(error)


def main():
    print("Welcome to Krisha Parser")
    base_url = 'https://kolesa.kz/cars/?'
    page_part = 'page='

    base_html = get_html(base_url)
    total_pages = get_total_pages(base_html)
    print(total_pages)
    global row
    global col
    global wb
    global sheet1

    sheet1.write(row, col, '#')
    col = col + 1
    sheet1.write(row, col, 'City')
    col = col + 1
    sheet1.write(row, col, 'Name')
    col = col + 1
    sheet1.write(row, col, 'Year')
    col = col + 1
    sheet1.write(row, col, 'Shell')
    col = col + 1
    sheet1.write(row, col, 'Engine volume, L')
    col = col + 1
    sheet1.write(row, col, 'Mileage')
    col = col + 1
    sheet1.write(row, col, 'Transmission')
    col = col + 1
    sheet1.write(row, col, 'Rudder')
    col = col + 1
    sheet1.write(row, col, 'Color')
    col = col + 1
    sheet1.write(row, col, 'Gear')
    col = col + 1
    sheet1.write(row, col, 'CustomsCleared')
    col = col + 1
    sheet1.write(row, col, 'Price')
    col = col + 1
    row = row + 1
    col = 0
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    for i in range(0, total_pages):
        url_gen = base_url + page_part + str(i)
        html = get_html(url_gen)
        try:
            get_page_data(html)
        except Exception as error:
            print(error)


if __name__ == "__main__":
    main()
