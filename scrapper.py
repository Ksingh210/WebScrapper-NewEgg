from scrapperdb import connection
from mysql.connector import Error
from bs4 import BeautifulSoup as soup
import requests 
from datetime import date

URL = 'https://www.newegg.com/msi-geforce-rtx-2060-rtx-2060-gaming-z-6g/p/N82E16814137379?Description=gtx%202060&cm_re=gtx_2060-_-14-137-379-_-Product'
fetch = requests.get(URL)

bestsoup = soup(fetch.content, 'html.parser')

cost = bestsoup.find(itemprop="price").get('content')

def insert_data(pull_date,product,price):

    query = "INSERT INTO neweggws (pull_date,product, price) VALUES (%s, %s, %s)"

    args = (pull_date,product,price)

    cursor = connection.cursor()
    cursor.execute(query, args)

    if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
    else:
            print('last insert id not found')

    connection.commit()

def main():
    today = date.today()
    insert_data(today,'MSI GeForce RTX 2060',cost)

if __name__ == '__main__':
    main()