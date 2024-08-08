from scrape_functions.Digistyle import digistyle
from scrape_functions.Mootanroo import mootanroo
from scrape_functions.Roja import Roja
from scrape_functions.Timcheh import Timcheh
from .email import send_mail
from utils import *

Roja_urls = [
    'https://rojashop.com/shop/cosmetic', # Lavazem Arayesh
    'https://rojashop.com/shop/hair', # Poost o Moo
    'https://rojashop.com/shop/electronic-appliances', # Electronics
    'https://rojashop.com/shop/fragrances' # Perfume
]
Timcheh_urls = [
    'https://timcheh.com/search/category-digital', # Digital
    'https://timcheh.com/search/category-home-and-kitchen', # Home and Kitchen
    'https://timcheh.com/search/category-car-tool-work' # Tools
]

###############
# replace the target link for the other two functions
###############


Roja_data = Roja(Roja_urls[0], 5)

df = pd.DataFrame(Roja_data)
df.drop_duplicates(inplace=True)
df.to_excel('Roja.xlsx')


Timcheh_data = Timcheh(Timcheh_urls[0], 5)

df = pd.DataFrame(Timcheh_data)
df.drop_duplicates(inplace=True)
df.to_excel('Timcheh.xlsx')


Digistyle_data = digistyle(5)

df = pd.DataFrame(Digistyle_data)
df.to_excel('Digistyle.xlsx')


Mootanroo_data = mootanroo(5)

df = pd.DataFrame(Mootanroo_data)
df.drop_duplicates(inplace=True)
df.to_excel('Mootanroo.xlsx')


# send_mail('./Roja.xlsx', 'example@gmail.com')