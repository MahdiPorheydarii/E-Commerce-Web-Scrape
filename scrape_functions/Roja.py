from utils import *

def Roja(url, n):
    urls = [f'{url}?page={x}' for x in range(1, n+1)]

    dt = ''
    for i in urls:
        dt += requests.get(i, verify=False).text

    products = []
    soup = BeautifulSoup(dt, 'html.parser')
    prods = soup.find('div', {'class': 'products_container'})
    prods = soup.find_all('div', class_='productct')

    for product_div in prods:
        try:
            product = {}
            
            product['id'] = product_div['data-id']
            product['name'] = product_div.find('a', class_='productLink').find('span').text
            product['image_url'] = product_div.find('img', class_='lazy')['data-src']
            product['price'] = product_div.find('span', class_='sale-price').text.strip()
            product['url'] = product_div.find('a', class_='productLink')['href']
            
            if product not in products:
                products.append(product)
        except:
            continue

    return products