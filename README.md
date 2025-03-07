# E-commerce Reviews Scraping

This Python project scrapes customer reviews from an e-commerce website (or a local HTML file) and saves the extracted data into both **CSV** and **Excel** formats. It uses libraries like **BeautifulSoup**, **Pandas**, **Requests**, and **openpyxl** to achieve this.

## Requirements

Before using this project, ensure that **Python** is installed on your machine, and the necessary libraries are set up:

1. **Python Installation**:
   - Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
   - After installation, verify by running the following command in your terminal:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```
     This should print the Python version (e.g., `Python 3.x.x`).

2. **Library Installation**:
   The following Python libraries are required to run this project:
   - **pandas**: For handling and saving the scraped data.
   - **beautifulsoup4**: For parsing and extracting data from HTML.
   - **requests**: For sending HTTP requests to scrape data from a live URL.
   - **openpyxl**: For saving data to an Excel file.

   To install the required libraries, open your terminal and run the following command:
   
   ```bash
   pip install pandas beautifulsoup4 requests openpyxl
