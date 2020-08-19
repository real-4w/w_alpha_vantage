# w_alpha_vantage

Python wrapper for Alpha Vantage API. Get current share price or historic prices in a pandas dataframe.

The alpa_vantage.py script will ask for the sharesymbol and return the current shareprice and will also get the historic monthly time series for the closing price.

It will process the returning JSON into a Panda dataframe for easy processing & plotting.

I hope you get the gist and play with Alpha Vantage.

Requirements

1) Install python,  pandas  matplotlib and yaml
2) Get an Alpha Vantage API Key here : https://www.alphavantage.co/support/#api-key
3) Update the api_key_dev in alpha.yaml wiht your own API key.
4) run alpha_vantage.py.


