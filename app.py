#This is a Stock Market dashboard to show shome charts and data on some stock

#Import the libraries
import streamlit as st
import pandas as pd
from PIL import Image

#Add a title and an image
st.title("Stock Market Agent")
st.write("""
Visually show a data on a stock! 
""")

# image = Image.open("/home/x/Desktop/SMdashboard/stockhome.jpg")
# st.image(image, use_column_width=True)

#Create sidebar header
st.sidebar.header('User Input')

#Create function to get get the user input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-05-04")
    end_date = st.sidebar.text_input("End Date", "2021-05-04")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    return start_date, end_date, stock_symbol

#Create function to get the company name 
def get_company_name(symbol):
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'SBI':
        return "State Bank of India"
    elif symbol == 'TCS':
        return "Tata Consultancy Service"
    elif symbol == 'HDFC':
        return "HDFC Bank"
    elif symbol == 'BTC':
        return "Bitcoin"
    elif symbol == 'DOGE':
        return "DogeCoin"        
    else:
        return 'None'

#Create function get the proper company data and the proper time frame the user start date to the users end date
def get_data(symbol, start, end):

    #load the data
    if symbol.upper() == 'AMZN':
        df = pd.read_csv("stocks/AMZN.csv")
    elif symbol.upper() == 'SBI':
        df = pd.read_csv("/home/x/Desktop/myProjects/SMA/stocks/SBIN.NS.csv") 
    elif symbol.upper() == 'TCS':
        df = pd.read_csv("/home/x/Desktop/myProjects/SMA/stocks/TCS.NS.csv")      
    elif symbol.upper() == 'HDFC':
        df = pd.read_csv("/home/x/Desktop/myProjects/SMA/stocks/HDFCBANK.NS.csv")
    elif symbol.upper() == 'BTC':
        df = pd.read_csv("/home/x/Desktop/myProjects/SMA/stocks/BTC-USD.csv")
    elif symbol.upper() == 'DOGE':
        df = pd.read_csv("/home/x/Desktop/myProjects/SMA/stocks/DOGE-USD.csv")
    else:
        df = pd.DataFrame(columns = ['Date','Open','High','Low','Close','Adj Close','Volume'])

    #get the date_range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    #set the stat and end index row both to zero 
    start_row = 0
    end_row = 0

    #Start the date from the top of the data sets and go down to see if the users start is less than or equal to the date in the data set
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break 

    #Start from the bottom of the dataset and go up to see if the users end date is greater than or equal to the date in the data set
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) -1 - j
            break
    #Set the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row +1, :]

#get the users input
start, end, symbol = get_input()
#get the data 
df = get_data(symbol, start, end)
#get the compnay name 
company_name = get_company_name(symbol.upper())

#Display the close price
st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])

#Display the volume 
st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

#get statistics on the data
st.header('Data statistics')
st.write(df.describe())
