from flask import Flask, request, render_template,redirect,url_for
app = Flask(__name__)
import pickle


#model = pickle.load(open('model.pkl','rb'))

import pandas as pd
import pymysql as pms
import numpy as np

def model(features):
    import pandas as pd
    data = pd.read_csv('C:\\Users\\admin\\Downloads\\heart.csv')
    
    x = data.iloc[:,:-1].values
    y = data.iloc[:,-1].values
    
    from sklearn.model_selection import train_test_split
    
    x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.25,random_state=0)
    
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    
    from sklearn.linear_model import LogisticRegression
    reg = LogisticRegression()
    reg.fit(x_train,y_train)
    
    features=np.reshape(np.array(features),(1,-1))
    prediction = reg.predict(features)
    return prediction


# app code starts here
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def validate():
    conn = pms.connect(host="localhost",port=3306,user="root",
                       password="Balavidyamandir03/",db="dbms")

    sql="select * from doctor"
    df=pd.read_sql(sql,conn)
    data=[request.form["user"],request.form["password"]]
    print(data)
    if(data in df.values.tolist()):
        return render_template("main.html")
    else:
        return redirect(url_for("main"))

@app.route("/predict", methods=['post'])
def pred():
    features = [i for i in (request.form.values())]
    pred = model(features)
    if pred==0:
        val="Low"
    else:
        val="High"
    return render_template("success.html",data=val)
    
if __name__=='__main__':
    app.run(host='localhost',port=5000)

pickle.dump(model, open('model.pkl', 'wb'))





    
    
    
    
    
    
    
    