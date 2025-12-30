# Text Extraction from PDF with Regex
This repository contains Python code for automating the extraction of key billing information from invoices in PDF format using the pypdf library and regular expressions (UK bills taken as an example). The script processes sample bills to pull account numbers, billing periods, total costs, and energy consumption into a structured Pandas DataFrame for analysis.

### Objectives
The tool automates invoice data entry for handling bulk billing records, eliminating manual transcription errors. It targets structured bills with consistent layouts, extracting five core fields via regex patterns tailored to phrases like "customer reference number" and "Total to pay £X.XX".  

Supports operations workflows for vendor payment validation or cost analytics in an efficient manner.

###Requirements
- Python 3.8+ with libraries: ```pypdf```, ```numpy```, ```pandas```
- Sample invoice: sample_bill.pdf

### Usage Steps
1. Extract Raw Text: get_pdf_text() function reads PDF pages, cleans artifacts (commas, non-breaking spaces, extra whitespace), and concatenates into a single string.
2. Apply Regular Expressions: Five targeted regex patterns capture:
```python
account_no = r'customer reference number which is ([0-9]+\s[0-9]+\s[0-9]+)'
start_date = r'Bill period: ([0-9]+\s[A-Za-z]+\s[0-9]+) –'
end_date = r'Bill period: [0-9]+\s[A-Za-z]+\s[0-9]+ – ([0-9]+\s[A-Za-z]+\s[0-9]+)'
cost = r'Total to pay £([0-9]+\.[0-9]+)'
consumption = r'meter reading = ([0-9]*\.[0-9]+) kWh'
```
3. Parse and Structure: Convert dates with ```pd.to_datetime(dayfirst=True),``` floats for numerics, then build DataFrame.
4. Output: Display structured table ready for Excel export or dashboarding.

### Key Code Features
- PDF Text Extraction: PdfReader iterates pages, robust cleaning handles layout issues.
- Scalable: Function can be modified to accept directory path—loop over multiple PDFs for batch processing.

### Limitations and Extensions
- Layout Dependent: Fails if invoice format changes (e.g., "Account No:" vs "customer reference").
- Error Handling: Add ```try/except``` for missing fields; validate extracted values against ranges.
- Future: Extend the single invoice extraction to multiple invoices by looping over ```os.listdir()``` for batch processing.

### Usage
Tested with UK energy supplier (British Gas). Customize regex for other regions/vendors.
