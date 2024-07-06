# Import streamlit
import streamlit as st

# Import helper functions
from helper import *

##Title
st.markdown("<h1 style='text-align: center; color: #0000FF;'>Finanalyser</h1>", unsafe_allow_html=True)

# Add a description
st.markdown(
    """
    This app retrieves the stock information of the selected stock from the Bombay Stock Exchange (BSE) or the National Stock Exchange (NSE).
    """
)

# Fetch and store the stock data
stock_dict = fetch_stocks()

# Add a dropdown for selecting the stock
st.markdown("<h2 style='text-align: center; color: #0000FF;'>Select Stock</h2>", unsafe_allow_html=True)
stock = st.selectbox("Choose a stock", list(stock_dict.keys()))

# Add a selector for stock exchange
st.markdown("<h2 style='text-align: center; color: #0000FF;'>Select Stock Exchange</h2>", unsafe_allow_html=True)
stock_exchange = st.radio("Choose a stock exchange", ("BSE", "NSE"), index=0)

# Build the stock ticker
stock_ticker = f"{stock_dict[stock]}.{'BO' if stock_exchange == 'BSE' else 'NS'}"

# Fetch the info of the stock
try:
    stock_data_info = fetch_stock_info(stock_ticker)
except:
    st.error("Error: Unable to fetch the stock data. Please try again later.")
    st.stop()

# Display the basic information
st.markdown("<h3 style='text-align: center; color: #222222;'>Basic Information</h3>", unsafe_allow_html=True)
d_basic_info = pd.DataFrame({" ":["Symbol", "Currency", "Exchange"], "  ":[stock_data_info["Basic Information"]["symbol"], stock_data_info["Basic Information"]["currency"], stock_data_info["Basic Information"]["exchange"]]})
st.markdown(d_basic_info.style.set_properties(**{'color': '#0000FF','font-weight':'bold', 'text-align': 'left', 'width':'100%'}).hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)

# Display the market data
st.markdown("<h3 style='text-align: center; color: #222222;'>Market Data</h3>", unsafe_allow_html=True)
d_market_data = pd.DataFrame({" ":["Current Price", "Previous Close", "Open", "Day Low", "Day High", "Regular Market Previous Close", "Regular Market Open", "Regular Market Day Low", "Regular Market Day High", "52 Week Low", "52 Week High", "50 Day Average", "200 Day Average"], "  ":[stock_data_info["Market Data"]["currentPrice"], stock_data_info["Market Data"]["previousClose"], stock_data_info["Market Data"]["open"], stock_data_info["Market Data"]["dayLow"], stock_data_info["Market Data"]["dayHigh"], stock_data_info["Market Data"]["regularMarketPreviousClose"], stock_data_info["Market Data"]["regularMarketOpen"], stock_data_info["Market Data"]["regularMarketDayLow"], stock_data_info["Market Data"]["regularMarketDayHigh"], stock_data_info["Market Data"]["fiftyTwoWeekLow"], stock_data_info["Market Data"]["fiftyTwoWeekHigh"], stock_data_info["Market Data"]["fiftyDayAverage"], stock_data_info["Market Data"]["twoHundredDayAverage"]]})
st.markdown(d_market_data.style.set_properties(**{'color': '#0000FF','font-weight':'bold', 'text-align': 'left', 'margin-left': 'auto', 'margin-right': 'auto', 'width':'100%'}).hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)

# Display the volume and shares
st.markdown("<h3 style='text-align: center; color: #222222;'>Volumes and Shares</h3>", unsafe_allow_html=True)
d_volume_shares = pd.DataFrame({" ":["Volume", "Regular Market Volume", "Average Volume", "Average Volume 10 Days", "Average Daily Volume 10 Days", "Shares Outstanding", "Implied Shares Outstanding", "Float Shares"], "  ":[stock_data_info["Volume and Shares"]["volume"], stock_data_info["Volume and Shares"]["regularMarketVolume"], stock_data_info["Volume and Shares"]["averageVolume"], stock_data_info["Volume and Shares"]["averageVolume10days"], stock_data_info["Volume and Shares"]["averageDailyVolume10Day"], stock_data_info["Volume and Shares"]["sharesOutstanding"], stock_data_info["Volume and Shares"]["impliedSharesOutstanding"], stock_data_info["Volume and Shares"]["floatShares"]]})
st.markdown(d_volume_shares.style.set_properties(**{'color': '#0000FF','font-weight':'bold', 'text-align': 'left', 'margin-left': 'auto', 'margin-right': 'auto', 'width':'100%'}).hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)

# Display the dividends and yield
st.markdown("<h3 style='text-align: center; color: #222222;'>Dividends and Yields</h3>", unsafe_allow_html=True)
d_dividend_yield = pd.DataFrame({" ":["Dividend Rate", "Dividend Yield", "Payout Ratio"], "  ":[stock_data_info["Dividends and Yield"]["dividendRate"], stock_data_info["Dividends and Yield"]["dividendYield"], stock_data_info["Dividends and Yield"]["payoutRatio"]]})
st.markdown(d_dividend_yield.style.set_properties(**{'color': '#0000FF','font-weight':'bold', 'text-align': 'left', 'margin-left': 'auto', 'margin-right': 'auto', 'width':'100%'}).hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)

# Display the valuation and ratios
st.markdown("<h3 style='text-align: center; color: #222222;'>Valuation and Ratios</h3>", unsafe_allow_html=True)
d_valuation_ratios = pd.DataFrame({" ":["Market Cap", "Enterprise Value", "Price to Book", "Debt to Equity", "Gross Margins", "Profit Margins"], "  ":[stock_data_info["Valuation and Ratios"]["marketCap"], stock_data_info["Valuation and Ratios"]["enterpriseValue"], stock_data_info["Valuation and Ratios"]["priceToBook"], stock_data_info["Valuation and Ratios"]["debtToEquity"], stock_data_info["Valuation and Ratios"]["grossMargins"], stock_data_info["Valuation and Ratios"]["profitMargins"]]})
st.markdown(d_valuation_ratios.style.set_properties(**{'color': '#0000FF','font-weight':'bold', 'text-align': 'left', 'margin-left': 'auto', 'margin-right': 'auto', 'width':'100%'}).hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)

# Display the financial performance
st.markdown("<h3 style='text-align: center; color: #222222;'>Financial Performance</h3>", unsafe_allow_html=True)
d_financial_performance = pd.DataFrame({" ":["Total Revenue", "Revenue per Share", "Total Cash", "Total Cash per Share", "Total Debt", "Earnings Growth", "Revenue Growth", "Return on Assets", "Return on Equity"], "  ":[stock_data_info["Financial Performance"]["totalRevenue"], stock_data_info["Financial Performance"]["revenuePerShare"], stock_data_info["Financial Performance"]["totalCash"], stock_data_info["Financial Performance"]["totalCashPerShare"], stock_data_info["Financial Performance"]["totalDebt"], stock_data_info["Financial Performance"]["earningsGrowth"], stock_data_info["Financial Performance"]["revenueGrowth"], stock_data_info["Financial Performance"]["returnOnAssets"], stock_data_info["Financial Performance"]["returnOnEquity"]]})
st.markdown(d_financial_performance.style.set_properties(**{'color': '#0000FF','font-weight':'bold', 'text-align': 'left', 'margin-left': 'auto', 'margin-right': 'auto', 'width':'100%'}).hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)

# Display the cash flow
st.markdown("<h3 style='text-align: center; color: #222222;'>Cash Flow</h3>", unsafe_allow_html=True)
d_cash_flow = pd.DataFrame({" ":["Free Cash Flow", "Operating Cash Flow"], "  ":[stock_data_info["Cash Flow"]["freeCashflow"], stock_data_info["Cash Flow"]["operatingCashflow"]]})
st.markdown(d_cash_flow.style.set_properties(**{'color': '#0000FF','font-weight':'bold', 'text-align': 'left', 'margin-left': 'auto', 'margin-right': 'auto', 'width':'100%'}).hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)

# Display the analyst targets
st.markdown("<h3 style='text-align: center; color: #222222;'>Analyst Targets</h3>", unsafe_allow_html=True)
d_analyst_targets = pd.DataFrame({" ":["Target High Price", "Target Low Price", "Target Mean Price", "Target Median Price"], "  ":[stock_data_info["Analyst Targets"]["targetHighPrice"], stock_data_info["Analyst Targets"]["targetLowPrice"], stock_data_info["Analyst Targets"]["targetMeanPrice"], stock_data_info["Analyst Targets"]["targetMedianPrice"]]})
st.markdown(d_analyst_targets.style.set_properties(**{'color': '#0000FF','font-weight':'bold', 'text-align': 'left', 'margin-left': 'auto', 'margin-right': 'auto', 'width':'100%'}).hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)

