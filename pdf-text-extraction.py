from google.colab import drive

drive.flush_and_unmount()
dir = '/content/drive/MyDrive/ColabNotebooks'
drive.mount('/content/drive')

# import the required modules
from pypdf import PdfReader
import numpy as np
import pandas as pd
import datetime as dt
from io import StringIO
import re
import os

# define a function to extract text from invoices
def get_pdf_text(directory):
    result = []
    reader = PdfReader(f'{directory}/Text Extraction Tool/sample_bill.pdf')
    for page in reader.pages:
        text = page.extract_text()
        text = text.replace(',', '')
        text = text.replace('\xa0', ' ')
        text = text.replace('\n', ' ')
        text = text.replace('  ', '')
        result = np.append(result, text)
    result = str(result)
    return result

text = get_pdf_text(dir)
print(text)

# use regular expressions to find out the account number, start date, end date, cost, and consumption for the billing period
account_no = re.findall(r'customer reference number which is ([0-9]+\s[0-9]+\s[0-9]+)', text)

start_date = re.findall(r'Bill period: ([0-9]+\s[A-Za-z]+\s[0-9]+) –', text)
start_date = pd.to_datetime(start_date, dayfirst=True)

end_date = re.findall(r'Bill period: [0-9]+\s[A-Za-z]+\s[0-9]+ – ([0-9]+\s[A-Za-z]+\s[0-9]+)', text)
end_date = pd.to_datetime(end_date, dayfirst=True)

cost = re.findall(r'Total to pay £([0-9]+\.[0-9]+)', text)
cost = [float(x) for x in cost]

consumption = re.findall(r'meter reading = ([0-9]*\.[0-9]+) kWh', text)
consumption = [float(y) for y in consumption]

print(account_no)
print(start_date)
print(end_date)
print(cost)
print(consumption)

# create a dataframe for the extracted text
df = pd.DataFrame({'Account_no': account_no, 'Start_date': start_date, 'End_date': end_date, 'Cost_(£)': cost, 'Consumption_kWh': consumption})
display(df)
