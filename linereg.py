from pymongo import MongoClient
import matplotlib as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
client=MongoClient()
db=client.zipwatch

zipcodelist=[10012,10007,10280,10005,10014,10018,10017,10020,10028,10075,10162,10069,10037,10033,10034,10474,10452,10464,
             10465,10453,10470,10471,11223,11234,11218,11228,11232,11692,11693,11695,11697,11690,11415,11421,11419,11424,11423,11435,11405,11431,11433,11439,11499,11379,11381,11428
                ,11429,11422,11005,11001,11002,11004,11414,11420,11425,11104,11377,11378,11109,11356,11357,11358,11359,11360,11351,11352,11386,11390,11380,11362,11363,11374,11430,11102
                ,11105,10044,11369,11370,11372,11371,10310,10308,10305,10307,10309]







for index in zipcodelist:
    cursor1=db.total_crime.find({"zipcode":index}).distinct("year")

    cursor=db.total_crime.find({"zipcode":index}).distinct("tc")

    xvalList=[]
    yvalList=[]

    for document1 in cursor1:
        xvalList.append(document1)

    for document2 in cursor:
        yvalList.append(document2)


    xvalarray=np.asarray(xvalList).astype(np.float)
    yvalarray=np.asarray(yvalList).astype(np.float)


    ones=np.ones(xvalarray.shape)
    x=np.array([xvalarray]).T

    regr=linear_model.LinearRegression()
    regr.fit(x,yvalarray)

    currGradRate=regr.predict(2016)
    predGradRate=regr.predict(2020)




    a=regr.coef_
    CurrTotalCrime=(a[0]*2016)+regr.intercept_
    PredTotalCrime=(a[0]*2020)+regr.intercept_
    cur=[]
    cur.append(float(CurrTotalCrime))
    pred=[]
    pred.append(float(PredTotalCrime))
    db.majorcrimeCurr.insert({"zipcode": index, "current": cur})
    db.majorcrimePred.insert({"zipcode": index, "predict": pred})

    print(index)
    print("Current " , CurrTotalCrime)
    print("Prediction ", PredTotalCrime)























