# Python Example project for basic ETL

import glob                         # this module helps in selecting files 
import pandas as pd                 # this module helps in processing CSV files
import xml.etree.ElementTree as ET  # this module helps in processing XML files.
from datetime import datetime

# ipython uzerinden dosya indirilmesi
# !wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip
# !unzip source.zip

logfile    = "logfile.txt"            # all event logs will be stored in this file
targetfile = "transformed_data.csv"   # file where transformed data is stored

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

# lines=True, line seperated json icin elzem
# olmamasi durumunda hata yiyorum
def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines=True)
    return dataframe

# Xml parse uzun versiyon
# def extract_from_xml(file_to_process):
#     dataframe = pd.DataFrame(columns=["name", "height", "weight"])
#     tree = ET.parse(file_to_process)
#     root = tree.getroot()
#     for person in root:
#         name = person.find("name").text
#         height = float(person.find("height").text)
#         weight = float(person.find("weight").text)
#         dataframe = dataframe.append({"name":name, "height":height, "weight":weight}, ignore_index=True)
#     return dataframe

# Xml parse kisa
def extract_from_xml(file_to_process):
    dataframe = pd.read_xml(file_to_process)
    return dataframe

# Composite EXTRACT fonksyonu
def extract():
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data
    
    #process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)
        
    #process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
    
    #process all xml files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
        
    return extracted_data

# TRANSFORM
def transform(data):
    data['height'] = round(data.height.astype(float) * 0.0254, 2)
    data['weight'] = round(data.weight.astype(float) * 0.45359237, 2)
    return data

# LOAD
def load(targetfile,data_to_load):
    data_to_load.to_csv(targetfile)  

# Logging
def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')

# Execution
log("ETL Job Started")

log("Extract phase Started")
extracted_data = extract()
log("Extract phase Ended")

log("Transform phase Started")
transformed_data = transform(extracted_data)
log("Transform phase Ended")

log("Load phase Started")
load(targetfile,transformed_data)
log("Load phase Ended")

log("ETL Job Ended")