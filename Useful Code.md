#Import data from Excel
INF_DF = pd.read_excel (r'/Users/JZ/Downloads/TEST_INFO.xlsx')
FINANCIALS_DF = pd.read_excel (r'/Users/JZ/Downloads/FIN_ALL.xlsx')
HIST_PRICE_DF = pd.read_excel (r'/Users/JZ/Downloads/PRICES_ALL.xlsx')


#Export data to excel
HIST_PRICE_DF.to_excel('/Users/JZ/Downloads/TEST_Prices.xlsx')  


#Remove duplicate
TICKER_ALL = list(dict.fromkeys(TICKER_ALL))
