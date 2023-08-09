import requests
import json
from bs4 import BeautifulSoup
from time import sleep

url = 'https://cryptoprices.com/wp-admin/admin-ajax.php?draw=1&columns%5B0%5D%5Bdata%5D=rank&columns%5B0%5D%5Bname%5D=rank&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=name&columns%5B1%5D%5Bname%5D=name&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=price_usd&columns%5B2%5D%5Bname%5D=price_usd&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=percent_change_1h&columns%5B3%5D%5Bname%5D=percent_change_1h&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=percent_change_24h&columns%5B4%5D%5Bname%5D=percent_change_24h&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=percent_change_7d&columns%5B5%5D%5Bname%5D=percent_change_7d&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=market_cap_usd&columns%5B6%5D%5Bname%5D=market_cap_usd&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=volume_usd_24h&columns%5B7%5D%5Bname%5D=volume_usd_24h&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=weekly&columns%5B8%5D%5Bname%5D=weekly&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=actions&columns%5B9%5D%5Bname%5D=actions&columns%5B9%5D%5Bsearchable%5D=true&columns%5B9%5D%5Borderable%5D=false&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=100&search%5Bvalue%5D=&search%5Bregex%5D=false&action=coinmc_table&id=18&watchlist=false&restrict=true&currency=USD&_=1691505402087'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def main():
    while True:
        res = requests.get(url, headers=headers).json()
        # soup = BeautifulSoup(res, "lxml")

        f = open('data.json')
        data = json.load(f)
        for coin in res["data"]:
            name_c = BeautifulSoup(coin["name"], "lxml").find(class_ = "coin-symbol").text
            price_c = BeautifulSoup(coin["price_usd"], "lxml").find_all("span")[-1].text
            if data[name_c] != price_c:
                print(f"Price edit {name_c}")
                data[name_c] = price_c
                with open('data.json', 'w') as f:
                    json.dump(data, f, indent=0)
        print("+")
        sleep(5)


if __name__ == '__main__':
    main()

