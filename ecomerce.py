from bs4 import BeautifulSoup
import pandas as pd
import os
import requests

# Headers for web scraping (useful only for online URLs)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Function to scrape reviews from local or online source
def scrape_reviews(target):
    reviews = []

    if os.path.exists(target):  # Check if target is a local file
        with open(target, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
    else:  # Assume it's a URL
        response = requests.get(target, headers=HEADERS)
        response.raise_for_status()  # Raise an error if the request fails
        soup = BeautifulSoup(response.text, "html.parser")

    # Extract reviews
    review_elements = soup.find_all("div", class_="review")
    for element in review_elements:
        try:
            username = element.find("span", class_="username").get_text(strip=True)
            rating = element.find("span", class_="rating").get_text(strip=True)
            comment = element.find("p", class_="comment").get_text(strip=True)
            reviews.append({
                "Username": username,
                "Rating": rating,
                "Comment": comment
            })
        except AttributeError:
            continue

    return reviews


# Target file or URL (Local file or URL)
TARGET_URL = "file2.html"  # Replace with the actual path to your file or URL

# Scrape the reviews
reviews_data = scrape_reviews(TARGET_URL)

# Save data to CSV and Excel
if reviews_data:
    # Convert to a DataFrame
    df = pd.DataFrame(reviews_data)

    # Save to CSV
    csv_file = "customer_reviews.csv"
    df.to_csv(csv_file, index=False, encoding="utf-8")
    print(f"Reviews have been saved to {csv_file}")

    # Save to Excel
    excel_file = "customer_reviews.xlsx"
    df.to_excel(excel_file, index=False, engine="openpyxl")  # Use 'openpyxl' for Excel files
    print(f"Reviews have been saved to {excel_file}")
else:
    print("No reviews found.")
