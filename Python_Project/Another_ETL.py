import glob
import pandas as pd
from datetime import datetime

# Url's:
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/bank_market_cap_1.json
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/bank_market_cap_2.json
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Final%20Assignment/exchange_rates.csv

def extract_from_json(file_to_process):
    # lines=True degil cunku dosyalar newLine seperated degil.
    dataframe = pd.read_json(file_to_process)
    return dataframe

columns=['Name','Market Cap (US$ Billion)']

def extract():
    jsonDf = pd.DataFrame(columns = columns)
    jsonDf = pd.concat([jsonDf,extract_from_json(
        '.\\Python_Project\\Final_Files\\bank_market_cap_1.json')])
    return jsonDf

df = pd.read_csv('.\\Python_Project\\Final_Files\\exchange_rates.csv', names=['Rates'], header=0)
exchange_rate = df.loc['GBP'].values[0]
print('Value of GBP is:' + str(exchange_rate))

# TODO: Amount of $ is not correct
def transform(df):
    returnDf = df.copy()
    returnDf.columns = ['Name','Market Cap (GBP$ Billion)']
    returnDf['Market Cap (GBP$ Billion)'] = round(
        returnDf['Market Cap (GBP$ Billion)'].astype(float) * exchange_rate, 3)
    return returnDf

def load(df):
    # Write your code here
    df.to_csv('.\\Python_Project\\Final_Files\\bank_market_cap_gbp.csv',index=False)

def log(message):
    now = datetime.now()
    date = now.strftime('%Y-%m-%d')
    dateTime = now.strftime('%Y-%m-%d / %H:%M:%S')
    path = '.\\Python_Project\\Final_Files\\'
    logFile = path + date + '-Log.txt'
    with open(logFile, 'a') as file:
        file.write(dateTime + '\t' + message + '\n')


# Execution
log("ETL Job Started")

log("Extract phase Started")
extracted_data = extract()
log("Extract phase Ended")

log("Transform phase Started")
transformed_data = transform(extracted_data)
log("Transform phase Ended")

log("Load phase Started")
load(transformed_data)
log("Load phase Ended")

log("ETL Job Ended")