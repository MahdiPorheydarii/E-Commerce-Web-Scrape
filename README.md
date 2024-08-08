# Multi-Site Web Scraper

This project is a Python-based web scraper that extracts product information from multiple e-commerce websites. It uses `requests` and `BeautifulSoup` for web scraping and saves the collected data to Excel files. 

## Features

- **Scrapes data** from various e-commerce websites, including Digistyle, Mootanroo, Roja, and Timcheh.
- **Saves data** into separate Excel files for each site.
- **Sends email notifications** with attached Excel files.

## Technologies Used

- **Python**: Programming language used for the scraper.
- **requests**: For making HTTP requests to web pages.
- **BeautifulSoup**: For parsing and extracting data from HTML.
- **pandas**: For data manipulation and saving to Excel.
- **smtplib**: For sending email notifications (optional).

## Setup and Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/multi-site-web-scraper.git
    cd multi-site-web-scraper
    ```

2. **Install dependencies**:

    Make sure you have `requests`, `beautifulsoup4`, `pandas`, and `openpyxl` installed. You can install them using pip:

    ```bash
    pip install requests beautifulsoup4 pandas openpyxl
    ```

3. **Configure email settings** (if you want to use email notifications):

    Edit the `send_mail` function in `email.py` with your SMTP server details and credentials.

## Usage

1. **Update the target URLs** for the scraping functions in `main.py` if necessary. The current setup scrapes the following sites:
   - **Roja**
   - **Timcheh**
   - **Digistyle**
   - **Mootanroo**

2. **Run the scraper**:

    ```bash
    python main.py
    ```

    This will generate Excel files with the scraped data:
    - `Roja.xlsx`
    - `Timcheh.xlsx`
    - `Digistyle.xlsx`
    - `Mootanroo.xlsx`

3. **Send email notifications**:

    Uncomment the `send_mail` function call in `main.py` and specify the email address to which the reports should be sent:

    ```python
    # send_mail('./Roja.xlsx', 'example@gmail.com')
    ```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
