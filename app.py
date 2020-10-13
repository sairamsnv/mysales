from flask import Flask,render_template,request,jsonify
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import datetime
df=pd.read_csv(r'D:\sairam\vise.csv')
df['date']=pd.to_datetime(df['date'])
df.set_index('date',inplace=True)
import statsmodels.api as sm
model=sm.tsa.statespace.SARIMAX(df['sales'],order=(3,1,3),seasonal_order=(3,1,3,12))
results=model.fit()
from pandas.tseries.offsets import DateOffset
future_dates=[df.index[-1]+ DateOffset(months=x)for x in range(0,24)]
future_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)
futuredata_df=pd.concat([df,future_df])

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])



def fun():
    #results.predict('2023-01-01')
    return render_template('my.html')

@app.route('/sai/',methods=['POST'])

def fun1():
    path =request.form['exp']
    #sd=path.append('')
    #print(sd)
    predict=results.predict(path)
    return render_template('mydisplay.html',value='orders{}'.format(predict))




if __name__ == "__main__":
    app.run(debug=True)