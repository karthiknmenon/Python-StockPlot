import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    

def graph_data(stock):
    s=raw_input("\n Enter stock name(for Indian stocks enter NSE:STOCKNAME) :")
    stock_price_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+s+'&apikey=Z1W9S4PPSIBEP7QI&datatype=csv'
    source_code = urllib.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source[1:]:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: bytespdate2num('%Y-%m-%d')})

    plt.plot_date(date, closep,'-', label='Price', color='#DC143C')
 
    plt.xlabel('DATE')
    plt.ylabel('PRICE')
    plt.title('STOCK PRICE')
    plt.legend()
    plt.show()


graph_data('s')
