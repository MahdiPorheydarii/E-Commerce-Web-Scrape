from utils import *

def mootanroo(page_number):
    url = f"https://mootanroo.com/makeup?pn={page_number}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    product_containers = soup.find_all('article', class_='group border-gray-light product-cards-border bg-white')
    
    product_names = []
    original_prices = []
    discounted_percentages = []
    product_links = []
    
    for product in product_containers:
        name_tag = product.find('p', class_='text-gray-p text-link h-[48px] text-ellipsis overflow-hidden leading-6')
        name = name_tag.text.strip()
        
        original_price_tag = product.find('p', class_='mt-0.5 text-link text-gray-disabled line-through font-normal')
        original_price = int(original_price_tag.text.strip('').replace(',', '')) if original_price_tag else 0

        discount_tag = product.find('div', class_='flex px-1 h-[18px] mr-1.5 items-center justify-center text-center bg-red-main text-white rounded-[4px]')
        discount = int(discount_tag.text.strip()[1:]) if discount_tag else 0
        

        
        link_tag = product.find('a', href=True)
        link = f"https://mootanroo.com{link_tag['href']}"
        
        product_names.append(name)
        original_prices.append(original_price)
        discounted_percentages.append(discount)
        product_links.append(link)
    
    return product_names, original_prices, discounted_percentages, product_links
