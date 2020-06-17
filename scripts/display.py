import os,sys
import pandas
import numpy
import matplotlib.pylab as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d 
from ctypes import cast, py_object


def main():

    df = pandas.read_csv('CME_ATM_VolCube_20200610.csv')
    print(df)
    ls = list(1,2,3,4)
    print(ls)
#     try:
#         if(len(sys.argv)>1):
#             QuoteData = sys.argv[1]
#         else:
#             QuoteData = 'QuoteData.dat'

#         qd = open(QuoteData, 'r')
#         qd_head = []
#         qd_head.append(qd.readline())
#         qd_head.append(qd.readline())
#         qd.close()
#     except:
#         sys.stderr.write("Usage: implied_volatility.py QuoteData.dat\n")
#         sys.stderr.write("Couldn't read QuoteData")
#         sys.exit(1)

#     print("Implied Volatility for %s %s" % (qd_head[0].strip(), qd_head[1]))

#     # Parse the header information in QuotaData
#     first = qd_head[0].split(',')
#     second = qd_head[1].split()
#     qd_date = qd_head[1].split(',')[0]
    
#     company = first[0]
#     underlyingprice = float(first[1])
#     month, day = second[:2]
#     today = cumulative_month[month] + int(day) - 30
#     current_year = int(second[2])

#     def getExpiration(x):
#         monthday = x.split()
#         adate = monthday[0] + ' ' + monthday[1]
#         if adate not in dates:
#             dates.append(adate)
#         return (int(monthday[0]) - (current_year % 2000)) * 365 + cumulative_month[monthday[1]]

#     def getStrike(x):
#         monthday = x.split()
#         return float(monthday[2])

#     data = pandas.io.parsers.read_csv(QuoteData, sep=',', header=2, na_values=' ')

#     # Need to fill the NA values in dataframe
#     data = data.fillna(0.0)

#     # Let's look at data where there was a recent sale 
# #    data = data[data.Calls > 0]
#     data = data[(data['Last Sale'] > 0) | (data['Last Sale.1'] > 0)]

#     # Get the Options Expiration Date
#     exp = data.Calls.apply(getExpiration)
#     exp.name = 'Expiration'

#     # Get the Strike Prices
#     strike = data.Calls.apply(getStrike)
#     strike.name = 'Strike'

#     data = data.join(exp).join(strike)

#     print('Calculating Implied Vol of Calls...')
#     impvolcall = pandas.Series(pandas.np.zeros(len(data.index)),
#                                index=data.index, name='impvolCall')
#     for i in data.index:
#         impvolcall[i] = (calcvol(data.Expiration[i],
#                                  data.Strike[i],
#                                  today,
#                                  underlyingprice,
#                                  (data.Bid[i] + data.Ask[i]) / 2, Nag_Call))

#     print('Calculated Implied Vol for %d Calls' % len(data.index))
#     data = data.join(impvolcall)

#     print('Calculating Implied Vol of Puts...')
#     impvolput = pandas.Series(numpy.zeros(len(data.index)),
#                               index=data.index, name='impvolPut')

#     for i in data.index:
#         impvolput[i] = (calcvol(data.Expiration[i],
#                                 data.Strike[i],
#                                 today,
#                                 underlyingprice,
#                                 (data['Bid.1'][i] + data['Ask.1'][i]) / 2.0, Nag_Put))

#     print('Calculated Implied Vol for %i Puts' % len(data.index))

#     data = data.join(impvolput)
#     fig = plt.figure(1)
#     fig.subplots_adjust(hspace=.4, wspace=.3)

#     # Plot the Volatility Curves
#     # Encode graph layout: 3 rows, 3 columns, 1 is first graph.
#     num = 331
#     max_xticks = 4
    
#     for date in dates:
#         # add each subplot to the figure
#         plot_year, plot_month = date.split()
#         plot_date = (int(plot_year) - (current_year % 2000)) * 365 + cumulative_month[plot_month]
#         plot_call = data[(data.impvolCall > .01) &
#                        (data.impvolCall < 1) &
#                        (data.Expiration == plot_date) &
#                        (data['Last Sale'] > 0)]
#         plot_put = data[(data.impvolPut > .01) &
#                         (data.impvolPut < 1) &
#                         (data.Expiration == plot_date) &
#                         (data['Last Sale.1'] > 0)]

#         myfig = fig.add_subplot(num)
#         xloc = plt.MaxNLocator(max_xticks)
#         myfig.xaxis.set_major_locator(xloc)
#         myfig.set_title('Expiry: %s 20%s' % (plot_month, plot_year))
#         myfig.plot(plot_call.Strike, plot_call.impvolCall, 'pr', label='call')
#         myfig.plot(plot_put.Strike, plot_put.impvolPut, 'p', label='put')
#         myfig.legend(loc=1, numpoints=1, prop={'size': 10})
#         myfig.set_ylim([0,1])
#         myfig.set_xlabel('Strike Price')
#         myfig.set_ylabel('Implied Volatility')
#         num += 1

#     plt.suptitle('Implied Volatility for %s Current Price: %s Date: %s' %
#                  (company, underlyingprice, qd_date))
    

#     print("\nPlotting Volatility Curves/Surface")
#     """
#     The code below will plot the Volatility Surface
#     It uses e02ca to fit with a polynomial and e02cb to evalute at 
#     intermediate points
#     """ 

#     m = numpy.empty(len(dates), dtype=nag_int_type())
#     y = numpy.empty(len(dates), dtype=numpy.double)
#     xmin = numpy.empty(len(dates), dtype=numpy.double)    
#     xmax = numpy.empty(len(dates), dtype=numpy.double)
 
#     data = data.sort('Strike') # Need to sort for NAG Algorithm

#     k = 3   # this is the degree of polynomial for x-axis (Strike Price)
#     l = 3   # this is the degree of polynomial for y-axis (Expiration Date)

#     i = 0

#     for date in dates:
#         plot_year, plot_month = date.split()
#         plot_date = (int(plot_year) - (current_year % 2000)) * 365 + cumulative_month[plot_month]
        
#         call_data = data[(data.Expiration == plot_date) & 
# 				(data.impvolPut > .01) & 
# 				(data.impvolPut < 1) &
#                                 (data['Last Sale.1'] > 0)]
         
#         exp_sizes = call_data.Expiration.size
#         if(exp_sizes > 0):       
#             m[i] = exp_sizes
#             n = len(dates)

#             if(i == 0):
#                 x = numpy.array(call_data.Strike)
#                 call = numpy.array(call_data.impvolPut)
#                 xmin[0] = x.min()
#                 xmax[0] = x.max()
#             else:
#                 x2 = numpy.array(call_data.Strike)
#                 x = numpy.append(x,x2)
#                 call2 = numpy.array(call_data.impvolPut)
#                 call = numpy.append(call,call2)
#                 xmin[i] = x2.min()
#                 xmax[i] = x2.max()
#             y[i] = plot_date-today
#             i+=1
#     nux = numpy.zeros(1,dtype=numpy.double)
#     nuy = numpy.zeros(1,dtype=numpy.double)
#     inux = 1
#     inuy = 1

#     if(len(dates) != i):
#         print("Error with data: the CBOE may not be open for trading or one expiration date has null data")
#         return 0
#     weight = numpy.ones(call.size, dtype=numpy.double)

#     output_coef = numpy.empty((k + 1) * (l + 1),dtype=numpy.double)
   

#     nStrikes = 100 # number of Strikes to evaluate    
#     spacing = 20 # number of Expirations to evaluate
    
#     for i in range(spacing):
#         mfirst = 1	
#         mlast = nStrikes
#         xmin = data.Strike.min()
#         xmax = data.Strike.max()
         
#         x = numpy.linspace(xmin, xmax, nStrikes)

#         ymin = data.Expiration.min() - today
#         ymax = data.Expiration.max() - today
      
#         y = (ymin) + i * numpy.floor((ymax - ymin) / spacing) 

#         fx=numpy.empty(nStrikes)
#         fail=quiet_fail()

#         e02cbc(mfirst,mlast,k,l,x,xmin,xmax,y,ymin,ymax,fx,output_coef,fail)
        
#         if(fail.code != 0):
#             print(fail.message)
        
#         if 'xaxis' in locals():
#             xaxis = numpy.append(xaxis, x)
#             temp = numpy.empty(len(x))
#             temp.fill(y)
#             yaxis = numpy.append(yaxis, temp)    
#             for j in range(len(x)):
#                 zaxis.append(fx[j])
#         else:
#             xaxis = x
#             yaxis = numpy.empty(len(x), dtype=numpy.double)
#             yaxis.fill(y)
#             zaxis = []
#             for j in range(len(x)):
#                 zaxis.append(fx[j])
   
#     fig = plt.figure(2)
#     ax = fig.add_subplot(111, projection='3d')

#     # A try-except block for Matplotlib
#     try:
#         ax.plot_trisurf(xaxis, yaxis, zaxis, cmap=cm.jet)
#     except AttributeError:
#         print ("Your version of Matplotlib does not support plot_trisurf")
#         print ("...plotting wireframe instead")
#         ax.plot(xaxis, yaxis, zaxis)
    
#     ax.set_xlabel('Strike Price')
#     ax.set_ylabel('Days to Expiration')
#     ax.set_zlabel('Implied Volatility for Put Options')
#     plt.suptitle('Implied Volatility Surface for %s Current Price: %s Date: %s' %
#                  (company, underlyingprice, qd_date))
    
#     plt.show()    

if __name__ == "__main__":
    main()