#alphavantage debug
#https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey=8C7LNHUO0MZEPUTC
import requests, json
import pandas as pd
import matplotlib.pyplot as plt 
import time                                                                             # delays
import pathlib
import yaml                                                                             # import pyyaml package
#=== Function to get real time stock value from Alphavantage ===============================================
def RealTimeSharePrice (stock_symbol, api_key) :
    '''This function loads the shareprice from alphavantage'''
    base_url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE"
    main_url = base_url + "&symbol=" + stock_symbol + "&apikey=" + api_key
    req_ob = requests.get(main_url)                     #get method of requests module & return response object
    result = req_ob.json()                              #json method return json format data into python dictionary data typ & result contains list of nested dictionaries
    if debug == True : 
        print("Result before parsing the json data :\n", result)
        print("Parsed as :\n", result["Global Quote"])
        print("Lenght ", len(result["Global Quote"]))
    if len(result["Global Quote"]) > 0: 
        share_price = float(result["Global Quote"]['05. price'])
        print("Realtime share price for", result["Global Quote"]["01. symbol"], "price", result["Global Quote"]["05. price"], "change", result["Global Quote"]["09. change"])
    else:
        share_price = float(0)
    return(share_price)
#===========================================================================================================
def HistoricSharePrice (stock_symbol, api_key) :
    '''This function loads the hsitoric shareprice from alphavantage'''
    base_url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY"
    main_url = base_url + "&symbol=" + stock_symbol + "&apikey=" + api_key
    req_ob = requests.get(main_url)                     #get method of requests module & return response object
    result = req_ob.json()                              #json method return json format data into python dictionary data typ & result contains list of nested dictionaries
    hsp_df=pd.DataFrame.from_dict(result['Monthly Time Series'], orient="index")  # json to df       
    hsp_df.index = pd.to_datetime(hsp_df.index, format='%Y-%m-%d')           #https://stackoverflow.com/questions/47124440/build-pandas-dataframe-from-json-data#47560590
    hsp_df.index.name = 'Date'
    hsp_df['1. open'] = hsp_df['1. open'].astype(float)
    hsp_df['2. high'] = hsp_df['2. high'].astype(float)
    hsp_df['3. low'] = hsp_df['3. low'].astype(float)
    hsp_df['4. close'] = hsp_df['4. close'].astype(float)
    if debug == True : 
        print(hsp_df[['1. open', '4. close']])
    return(hsp_df)
#===========================================================================================================
def PlotHistoricSharePrice (stock_symbol, hsp_df) :
    fig1, ax1 = plt.subplots(1,1)
    title1 = "Historic share price"
    fig1.canvas.set_window_title(title1)
    hsp_df.plot(kind='line', use_index=True, y=['4. close'], ax=ax1, title=title1)
    plt.legend([stock_symbol], loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.subplots_adjust(bottom=0.15, left=0.05, right=0.85, top=0.95)
    return()
#===========================================================================================================
def AskInputShareCode (): 
    stock_symbol =input("Please enter stock symbol to test on AlphaVantage :")
    return (stock_symbol)
#===========================================================================================================
def ProcessYAML (yaml_file) :
    '''This function opens the yaml file and returns the data object'''
    with open(yaml_file) as f:
        y_data = yaml.load(f, Loader=yaml.FullLoader)
        debug = y_data['debug']
        if debug == True : print("YAML file:\n", y_data)
    return (y_data)    
#===========================================================================================================
yaml_data = ProcessYAML('alpha.yaml')                                     #yaml settings are global variables
debug = yaml_data['debug']                                                #debug mode?
plot = yaml_data['plot']                                                  #plot mode?  
copy_to_file = yaml_data['copy_to_file']                                  #file output
api_key = yaml_data['api_key_dev']
#===========================================================================================================
if __name__ == "__main__":                                                    #only run when this is called by itself and not imported
    stock_symbol = AskInputShareCode() 
    if copy_to_file == True : import w_logger                                 #send a copy of stout to w_output.log
    if debug == True : print (api_key)
    share_price = RealTimeSharePrice(stock_symbol, api_key)
    hist_share_price_df = HistoricSharePrice (stock_symbol, api_key)
    if plot == True : 
        PlotHistoricSharePrice(stock_symbol, hist_share_price_df)
        plt.show()
    print("===========")