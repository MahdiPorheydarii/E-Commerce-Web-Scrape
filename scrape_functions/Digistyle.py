from utils import *

def digistyle(page_num):
    url = "https://www.digistyle.com/category-men-clothing/?pageno=" + str(page_num)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.find_all('div', class_="cp-card cp-card--product-card js-cro-product")

    product_names = []
    product_prices = []
    product_urls = []

    for product in products:
        brand_tag = product.find('a', class_='c-product-card__brand ')
        brand = brand_tag.strip() if brand_tag else ''

        name_tag = product.find('a', class_='c-product-card__title ga-product-impression')
        name = name_tag.text.strip() if name_tag else 'No name'

        price_tag = product.find('div', class_='c-product-card__selling-price c-product-card__currency')
        price = price_tag.text.strip() if price_tag else 'ناموجود'
        
        url_tag = product.find('a', href=True)
        url = url_tag['href'] if url_tag else 'No link'


        product_names.append(name)
        product_prices.append(price)
        product_urls.append(url)

    return product_names, product_prices, product_urls