# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:44:13 2018

@author: academy
"""

import NSEpy_Download as nd
from datetime import date ,timedelta
import pandas as pd

class get_stock_futures_continous():
    def __init__(self,stock,start,end):
        self.stock=stock
        self.start=start
        self.end=end
    def get_data(self):
        df=pd.DataFrame()
        months=self.end.month-self.start.month
        years=self.end.year-self.start.year
        total_months=months+12*years
        for i in range(total_months):
            if i==0:
              
                df=df.append(nd.get_nsepy_data(self.stock,self.start,self.end)\
                          .get_stock_futures(self.start.year,self.start.month))
            else:
                if (self.start.month+(i-1)%12)%12 !=0:
                    start_month=(self.start.month+(i-1)%12)%12
                    start_year= self.start.year+int((self.start.month+i-1)/12)

                else:
                    start_month=12
                    start_year= self.start.year+int((self.start.month+i-1)/12)-1

                if (self.start.month+(i)%12)%12 !=0:
                    end_month=(self.start.month+(i)%12)%12
                    end_year=self.start.year+int((self.start.month+i)/12)

                else:
                    end_month=12
                    end_year=self.start.year+int((self.start.month+i)/12)-1

                df=df.append(nd.get_nsepy_data(self.stock,nd.get_expiry_date\
                                            (start_year,start_month)+timedelta(1),nd.get_expiry_date\
                                             (end_year,end_month)).\
                                             get_stock_futures(end_year,end_month))
        df=df.append(nd.get_nsepy_data(self.stock,nd.get_expiry_date\
                                            (end_year,end_month)+timedelta(1),self.end).\
                                             get_stock_futures(self.end.year,self.end.month))


        return df


class get_stock_options_continous():
    def __init__(self,stock,start,end,strike,option_type='PE'):
        self.stock=stock
        self.start=start
        self.end=end
        self.strike=strike
        self.option_type=option_type
    def get_data(self):
        df=pd.DataFrame()
        months=self.end.month-self.start.month
        years=self.end.year-self.start.year
        total_months=months+12*years
        
        if self.option_type=='PE':
            for i in range(total_months):
                if i==0:
                  
                    df=df.append(nd.get_nsepy_data(self.stock,self.start,self.end)\
                              .get_stock_put(self.start.year,self.start.month,self.strike))
                else:
                    if (self.start.month+(i-1)%12)%12 !=0:
                        start_month=(self.start.month+(i-1)%12)%12
                        start_year= self.start.year+int((self.start.month+i-1)/12)
    
                    else:
                        start_month=12
                        start_year= self.start.year+int((self.start.month+i-1)/12)-1
    
                    if (self.start.month+(i)%12)%12 !=0:
                        end_month=(self.start.month+(i)%12)%12
                        end_year=self.start.year+int((self.start.month+i)/12)
    
                    else:
                        end_month=12
                        end_year=self.start.year+int((self.start.month+i)/12)-1
    
                    df=df.append(nd.get_nsepy_data(self.stock,nd.get_expiry_date\
                                                (start_year,start_month)+timedelta(1),nd.get_expiry_date\
                                                 (end_year,end_month)).\
                                                 get_stock_put(end_year,end_month,self.strike))
            df=df.append(nd.get_nsepy_data(self.stock,nd.get_expiry_date\
                                (end_year,end_month)+timedelta(1),self.end).\
                                 get_stock_put(self.end.year,self.end.month,self.strike))


        else:
            for i in range(total_months):
                if i==0:
                  
                    df=df.append(nd.get_nsepy_data(self.stock,self.start,self.end)\
                              .get_stock_call(self.start.year,self.start.month,self.strike))
                else:
                    if (self.start.month+(i-1)%12)%12 !=0:
                        start_month=(self.start.month+(i-1)%12)%12
                        start_year= self.start.year+int((self.start.month+i-1)/12)
    
                    else:
                        start_month=12
                        start_year= self.start.year+int((self.start.month+i-1)/12)-1
    
                    if (self.start.month+(i)%12)%12 !=0:
                        end_month=(self.start.month+(i)%12)%12
                        end_year=self.start.year+int((self.start.month+i)/12)
    
                    else:
                        end_month=12
                        end_year=self.start.year+int((self.start.month+i)/12)-1
    
                    df=df.append(nd.get_nsepy_data(self.stock,nd.get_expiry_date\
                                                (start_year,start_month)+timedelta(1),self.end).\
                                                 get_stock_call(end_year,end_month,self.strike))
            df=df.append(nd.get_nsepy_data(self.stock,nd.get_expiry_date\
                    (end_year,end_month)+timedelta(1),self.end).\
                     get_stock_call(self.end.year,self.end.month,self.strike))
 
        return df

























stock='PNB'
#index='NIFTY'
start=date(2001,2,25)
end=date(2018,3,1)
#expiry_month=3
#expiry_year=2018
#
data1=get_stock_futures_continous(stock,start,end).get_data()
#data2=get_stock_options_continous(stock,start,end,300,'CE').get_data()

data1.Close.plot()
#data2.Close.plot()