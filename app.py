from flask import Flask,render_template,request,make_response,session
import pymongo
import random
from time import time
from random import random
import json




app=Flask(__name__)
app.secret_key= "wikedcase"


#Database

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db=client['login']
mydata=db.information



#database2
client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
db=client['iot']
myvalue=db.values



#login page
@app.route('/',methods=['GET','POST'])

def fun():
    return render_template('my.html')

@app.route('/sai/',methods=['GET','POST'])
def fun2():
    session['name']=request.form['nam']
    name=session['name']
    password=request.form['pass']
    cd='wrong email or password'
    for record in mydata.find({'email':name,'password':password}):
        if bool(record)==True:
            return render_template('mainpage.html',si='{}'.format(name))    
        
    return render_template('my.html',ds='{}'.format(cd))

#register form and saving to data base
@app.route('/ram/',methods=['GET','POST'])
def fun3():
    return render_template('sign.html')

@app.route('/snv/',methods=['GET','POST'])
def fun4():
   firstname=request.form['fir']
   lastname=request.form['lst']
   email=request.form['em']
   password=request.form['pass']
   vrpass=request.form['vpass']
   per=request.form['opttick']
   cpid=request.form['cid']
   print(cpid)
   dp='password unmatched'
   if password==vrpass and per=='personal':
        User={
            'firstname':firstname,
            'lastname':lastname,
            'password':password,
            'email':email,
            }
        mydata.insert_one(User)
   elif password==vrpass and per=='bussiness':
       User={
            'firstname':firstname,
            'lastname':lastname,
            'password':password,
            'email':email,
            'company_id':cpid
            }
       mydata.insert_one(User)

   else:
       return render_template('sign.html',cc='{}'.format(dp))
   


   return render_template('my.html')
@app.route('/graphs/',methods=['GET','POST'])
def fun5():
    return render_template('live.html')

#this analytics graphs...
@app.route('/live-data')
def live_data():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000,random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

#getting devices page ...
@app.route('/getdev/',methods=['GET','POST'])
def fun6():
    return render_template('devices1.html')
#this function  are device data....
@app.route('/tees/',methods=['GET','POST'])
def fun7():
    if 'name' in session:
        df=session['name']

        fd='123432'
        dg='B Series LTE CAT1/3G/2G'
        sd='Tracking device'
        return render_template('mainpage.html',cg='{}'.format(fd),kl='{}'.format(sd),fd='{}'.format(dg),si='{}'.format(df))

@app.route('/tee/',methods=['GET','POST'])
def fun8():
    if 'name' in session:
        df=session['name']
        fd='123432'
        dg='B Series LTE CAT1/3G/2G'
        sd='Tracking device'
        return render_template('mainpage.html',ss='{}'.format(fd),sss='{}'.format(sd),ssss='{}'.format(dg),si='{}'.format(df))



@app.route('/act/',methods=['GET','POST'])
def fun9():
    tname=request.form['usr1']
    tno=request.form['usr2']
    lcap=request.form['usr3']
    mload=request.form['usr4']
    sensor1=request.form['op1']
    User={
            'truck name':tname,
            'truck no':tno,
            'load capicty':lcap,
            'max load':mload,
            'sensor1':sensor1,
            }
    myvalue.insert_one(User)
    #sensor2=request.form['op2']
   #sensor3=request.form['op3']
    #sensor4=request.form['op4']
    print(tname)
    print(tno)
    print(lcap)
    print(mload)
    print(sensor1)
    #print(sensor2)
    #print(sensor3)
   # print(sensor4)
    return render_template('mainpage.html')


if __name__ == "__main__":
    app.run(debug=True)