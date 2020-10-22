from flask import Flask,render_template,request,jsonify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import datetime
df=pd.read_csv(r'https://raw.githubusercontent.com/sairamsnv/mysales/main/nsales.csv')

import statsmodels.api as sm
from pandas.tseries.offsets import DateOffset

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])



def fun():
    #results.predict('2023-01-01')
    return render_template('my.html')

@app.route('/sai/',methods=['POST'])

def fun1():
    path =request.form['exp']
    val=request.form['cars']
    cus=request.form['train']
    print(cus)
    name=pd.get_dummies(df['name'])
    x=df.drop('name',axis=1)
    x=pd.concat([x,name],axis=1)
    iteam=pd.get_dummies(x['iteam'])
    y=x.drop('iteam',axis=1)
    y=pd.concat([y,iteam],axis=1)
    z=cus
    c=val
    if c=='RAK00001®' and z=='Smith East':
        df_smio=(y.loc[y['Smith Inc. : Smith East'] & y['RAK00001®']==1])
    elif c=='RAK00001®' and z=='Smith West':
        df_smio=(y.loc[y['Smith Inc. : Smith West'] & y['RAK00001®']==1])
    elif c=='RAK00001®' and z=='Fabre Enterprises':
        df_smio=(y.loc[y['Fabre Enterprises'] & y['RAK00001®']==1])
    elif c=='BBP00001' and z=='Fabre Enterprises':
        df_smio=(y.loc[y['Fabre Enterprises'] & y['BBP00001']==1])
    elif c=='RAK00001®' and z=='Smith Inc':
        df_smio=(y.loc[y['Smith Inc.'] & y['RAK00001®']==1])
    elif c=='BBP00001' and z=='Smith Inc':
        df_smio=(y.loc[y['Smith Inc.'] & y['BBP00001']==1])
    elif c=='BBP00001' and z=='Smith East':
        df_smio=(y.loc[y['Smith Inc. : Smith East'] & y['BBP00001']==1])
    elif c=='BBP00001' and z=='Smith West':
        df_smio=(y.loc[y['Smith Inc. : Smith West'] & y['BBP00001']==1])
    #else:
       # mess="CHECK THE GIVEN FIELDS"



    
    #else:
        #df_smio=(y.loc[y['Smith Inc. : Smith East'] & y['BBP00001']==1])
    
    df_smith_order=df_smio.drop(['Smith Inc.','Smith Inc. : Smith West','Smith Inc. : Smith East','BBP00001','RAK00001®','Fabre Enterprises'],axis=1)
    #print(df_smith_order)
    df_smith_order['date']=pd.to_datetime(df_smith_order['date'])
    df_smith_order.set_index('date',inplace=True)
    import statsmodels.api as sm
    model=sm.tsa.statespace.SARIMAX(df_smith_order,order=(1,1,1),seasonal_order=(1,1,1,12))
    results=model.fit()
    future_dates=[df_smith_order.index[-1]+ DateOffset(months=x)for x in range(0,24)]
    future_df=pd.DataFrame(index=future_dates[1:],columns=df_smith_order.columns)
    futuredata_df=pd.concat([df_smith_order,future_df])

    
    #sd=path.append('')
    #print(sd)
    predict=results.predict(path)
    cgi=predict.values
    mys=' '.join(map(str, cgi))
    return render_template('index1.html',value='{}'.format(mys),sd='{}'.format(val),ds='{}'.format(cus))




if __name__ == "__main__":
    app.run(debug=True)