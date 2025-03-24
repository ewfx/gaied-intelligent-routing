import re

# Extracts key fields like CUSIP, ISIN, Amount, and Date
def extract_key_data(text):
    cusip_match = re.search(r'CUSIP\s(\d+)', text)
    isin_match = re.search(r'ISIN\s(\w+)', text)
    amount_match = re.search(r'USD\s([\d,]+(?:\.\d{2})?)', text)
    date_match = re.search(r'(\d{1,2}-[A-Za-z]{3}-\d{4})', text)

    return {
        "CUSIP": cusip_match.group(1) if cusip_match else None,
        "ISIN": isin_match.group(1) if isin_match else None,
        "Amount": amount_match.group(1) if amount_match else None,
        "Date": date_match.group(1) if date_match else None,
    }
