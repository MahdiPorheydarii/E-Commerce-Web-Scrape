from bs4 import BeautifulSoup
import pandas as pd
import requests
from .email import send_mail
import warnings
from urllib3.exceptions import InsecureRequestWarning
warnings.filterwarnings('ignore', category=InsecureRequestWarning)

