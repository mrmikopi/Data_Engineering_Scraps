from locale import currency
import pyparsing as pp
import requests
import pandas as pd

# Api'den alinan doviz kur bilgilerini pandas dataframe'ine aktarir.
# String parsing islemi icin pyparsing kullanimi mecut.

# Api key: VgGBAEaPYFLPTNMQ6JRzk6Fq9BIoJs3z

# Write your code here
#Make sure to change ******* to your API key.
url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=VgGBAEaPYFLPTNMQ6JRzk6Fq9BIoJs3z" 
response = requests.get(url)
print('Api request status code: ' + str(response.status_code))

# Create DataFrame
columns = ['Rate']
df = pd.DataFrame(columns=columns)

# Split response into seperate lines
responseLines = response.text.split('\n')

# PyParsing Format
lineFormat = ("\"" + pp.Word(pp.alphas) + "\":" 
+ pp.Combine(pp.Word(pp.nums) + pp.Optional('.'+ pp.Word(pp.nums)))
+ pp.Optional('e-' + pp.Word(pp.nums)) 
+ pp.Optional(','))

# Iterate through meaningful lines
for line in responseLines[6:len(responseLines) - 3]:
    # PyParse
    # print(line)
    splitLine = lineFormat.parse_string(line)
    # New currency in dataFrame format
    newCurrency = pd.DataFrame(
        data=[float(splitLine[3])], columns=columns,index=[splitLine[1]])
    # Concat new currency df to original df
    df = pd.concat([df,newCurrency])

df['Rate'] = df['Rate'].astype(float)
print(df.dtypes)
