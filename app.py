import streamlit as st
import yfinance as yf
import datetime
st.write(""" # Stock Price Analyser """)
st.write(""" ## Apple's Stock price data """)

## get the data for Apple's stock
symbol = "AAPL"
symbol = st.selectbox(
    'which stock whould you wnt to analyse',('AAPL','GOOG','TSLA','MSFT','NFLX')
)

col1,col2=st.columns(2)
with col1:
    start_date=st.date_input("please enter start date",datetime.date(2019,7,6))
with col2:
    end_date=st.date_input("please enter end date",datetime.date(2019,7,10))

ticker_data= yf.Ticker(symbol)
ticker_df = ticker_data.history(period = "1d", start = start_date , end = end_date)
st.dataframe(ticker_df)

st.write(f""" ## {symbol} closing price chart price data """)
st.line_chart(ticker_df["Close"])
