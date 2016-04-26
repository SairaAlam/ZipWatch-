from pymongo import MongoClient
import matplotlib as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
client=MongoClient()
db=client.zipwatch

zipcodelist=[10013,10004,10006,10282,10038,10002,10003,10009,10011,10010,10001,10016,10022,10019, 10036, 10021, 10065
              , 10128, 10023, 10024, 10029, 10025, 10035, 10027, 10026, 10031, 10030, 10039, 10032,
             10040,10454,10455,10459,10451,10462,10472,10473,10456,10468,10466,10475,10457,10460,10469,10461,10461,
             10463,10467,10458,11224,11229,11235,11214,11210,11204,11219,11203,11226,11209,11220,11236,11230,11225,11212,11233,11208,11207,11239,11231,11213,11217,11215,11216,11221
             ,11237,11201,11205,11238,11211,11206,11222,11694,11691,11418,11416,11432,11451,11385,11426,11694,11691,11418,11416,11432,11451,11385,11426,
             11427, 11411, 11413, 11417, 11365,11366,11367,11101,11354,11355,11368,11373,11364,11361,11375,11412,11434,11436,
             11103,11106,10312,10304,10306,10301]







for index in zipcodelist:
    cursor1=db.total_crime.find({"zipcode":index}).distinct("year")
    cursor2=db.total_crime.find({"zipcode":index}).distinct("gradrate")
    cursor=db.total_crime.find({"zipcode":index}).distinct("tc")

    xvalList=[]
    yvalList=[]

    for document1 in cursor1:
        xvalList.append(document1)

    for document2 in cursor2:
        yvalList.append(document2)


    xvalarray=np.asarray(xvalList).astype(np.float)
    yvalarray=np.asarray(yvalList).astype(np.float)


    ones=np.ones(xvalarray.shape)
    x=np.array([xvalarray]).T

    regr=linear_model.LinearRegression()
    regr.fit(x,yvalarray)

    currGradRate=regr.predict(2016)
    predGradRate=regr.predict(2020)

    newylist=[]
    for document in cursor:
        newylist.append(document)

    newyarray=np.asarray(newylist).astype(np.float)
    x1valarray=np.asarray(xvalarray).astype(np.float)
    x2valarray=np.asarray(yvalarray).astype(np.float)

    ones=np.ones(x1valarray.shape)
    x=np.array([x1valarray,x2valarray]).T
    regr=linear_model.LinearRegression()
    regr.fit(x,newyarray)


    a=regr.coef_
    CurrTotalCrime=(a[0]*2016)+(a[1]*currGradRate)+regr.intercept_
    PredTotalCrime=(a[0]*2020)+(a[1]*predGradRate)+regr.intercept_
    cur=[]
    cur.append(float(CurrTotalCrime))
    pred=[]
    pred.append(float(PredTotalCrime))

    db.majorcrimeCurr.insert({"zipcode": index,"current":cur})
    db.majorcrimePred.insert({"zipcode":index,"predict":pred})
    print(index)
    print("Current " , CurrTotalCrime)
    print("Prediction ", PredTotalCrime)























