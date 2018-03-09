# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 10:11:24 2018

@author: academy
"""
from nsepy import history
from datetime import date ,timedelta
from nsepy.derivatives import get_expiry_date
import pandas as pd

class get_nsepy_data():
    def __init__(self,stock,start,end):
        self.stock=stock
        self.start=start
        self.end=end
    def get_stock_futures(self,expiry_year,expiry_month):
        expiry=get_expiry_date(expiry_year,expiry_month)
        df= pd.DataFrame()
        for i in range(8):
            if len(df)==0:
                try:
                    df=history.get_history(self.stock,self.start,self.end,\
                                   futures=True,\
                                   expiry_date=expiry-timedelta(i))
                except:
                    continue

        return df
        
    def get_stock_put(self,expiry_year,expiry_month,strike,):
        expiry=get_expiry_date(expiry_year,expiry_month)
        df= pd.DataFrame()
        for i in range(8):
            if len(df)==0:
                try:
                    df=history.get_history(self.stock,self.start,self.end,\
                                   option_type='PE',\
                                   expiry_date=expiry-timedelta(i),strike_price=strike)
                except:
                    continue

        return df
    def get_stock_call(self,expiry_year,expiry_month,strike):
        expiry=get_expiry_date(expiry_year,expiry_month)
        df= pd.DataFrame()
        for i in range(8):
            if len(df)==0:
                try:
                    df=history.get_history(self.stock,self.start,self.end,\
                                   option_type='CE',\
                                   expiry_date=expiry-timedelta(i),strike_price=strike)
                except:
                    continue

        return df
    def get_index_futures(self,expiry_year,expiry_month):
        expiry=get_expiry_date(expiry_year,expiry_month)
        df= pd.DataFrame()
        for i in range(8):
            if len(df)==0:
                try:
                    df=history.get_history(self.stock,self.start,self.end,\
                                   futures=True,index=True,\
                                   expiry_date=expiry-timedelta(i))
                except:
                    continue

        return df
        
    def get_index_put(self,expiry_year,expiry_month,strike):
        expiry=get_expiry_date(expiry_year,expiry_month)
        df= pd.DataFrame()
        for i in range(8):
            if len(df)==0:
                try:
                    df=history.get_history(self.stock,self.start,self.end,\
                                   option_type='PE',index=True,\
                                   expiry_date=expiry-timedelta(i),strike_price=strike)
                except:
                    continue

        return df
    def get_index_call(self,expiry_year,expiry_month,strike):
        expiry=get_expiry_date(expiry_year,expiry_month)
        df= pd.DataFrame()
        for i in range(8):
            if len(df)==0:
                try:
                    df=history.get_history(self.stock,self.start,self.end,\
                                   option_type='CE',index=True,\
                                   expiry_date=expiry-timedelta(i),strike_price=strike)
                except:
                    continue

        return df

stock='SBIN'
#index='NIFTY'
start=date(2017,2,1)
end=date(2018,3,1)
expiry_month=3
expiry_year=2018
#
#
data1=get_nsepy_data(stock,start,end).get_stock_futures(expiry_year,expiry_month)
#data2=get_nsepy_data(stock,start,end).get_stock_call(expiry_year,expiry_month,260)
#data3=get_nsepy_data(index,start,end).get_index_futures(expiry_year,expiry_month)
#data4=get_nsepy_data(index,start,end).get_index_put(expiry_year,expiry_month,10500)
#
