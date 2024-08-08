from utils import *
def Timcheh(url, n):
    urls = [f'{url}?page={x}' for x in range(1, n+1)]

    dt = ''
    for i in urls:
        dt += requests.get(i, verify=False).text
    products = []
    soup = BeautifulSoup(dt, 'html.parser')

    product_items = soup.find_all('li', class_=lambda x: x and x.startswith('category_styles_product_card_item__'))

    products = []
    for item in product_items:
        try:
            title = item.find('h3',class_= lambda x : x and x.startswith("styles_title__")).text.strip()

            product_url = 'https://timcheh.com' + item.find('a')['href']

            price = item.find('div', class_= lambda x : x and x.startswith("styles_price__")).text.strip()
            currency = item.find('div', class_= lambda x : x and x.startswith("styles_currency__")).text.strip()
            full_price = price + ' ' + currency

            products.append({'title': title, 'price': full_price, 'product_url': product_url})
        except:
            continue

    return products


