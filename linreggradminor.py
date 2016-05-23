from pymongo import MongoClient
import matplotlib as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
client=MongoClient()
db=client.zipwatch

zipcodelist=[10013,10004,10006,10282,10038,10002,10003,10009,10011,10010,10001,10016,10022,10019,
             10036, 10021,10128, 10023, 10024, 10029, 10025, 10035, 10027, 10026, 10031, 10030, 10039,
             10032,10040,10454,10459,10451,10462,10472,10473,10468,10466,10475,10457,10460,10469,10461,10461,10463,
             10467,10458,11221,11216,11215,11217,11213,11231, 11239,11207,11208,11233 ,11212,11230,11225,11209,11220,11236,11224,11229
    ,11235, 11214, 11210, 11204,11219, 11203, 11226,11237,11201,11205,11211 ,11206,11222  ,11691,11418,11416,11432,11385, 11411, 11413, 11365
    ,11366, 11367, 11354, 11355, 11368,11373,11364,11361,11375,11412,11434,11436,11103,11106,10312,10304,10306,10301,11238,11101,10456,11694]






for index in zipcodelist:
    cursor1=db.minor_crime.find({"zipcode":index}).distinct("year")
    cursor2=db.minor_crime.find({"zipcode":index}).distinct("gradrate")
    cursor=db.minor_crime.find({"zipcode":index}).distinct("tc")
    cursor3=db.minor_crime.find({"zipcode":index}).distinct("pop")
    cursor4 = db.minor_crime.find({"zipcode": index}).distinct("income")

    xvalList=[]
    yvalList=[]
    zvalList=[]
    wvalList=[]

    for document1 in cursor1:
        xvalList.append(document1)

    for document2 in cursor2:
        yvalList.append(document2)

    for document3 in cursor3:
        zvalList.append(document3)

    for document4 in cursor4:
        wvalList.append(document4)


    xvalarray=np.asarray(xvalList).astype(np.float)
    yvalarray=np.asarray(yvalList).astype(np.float)
    zvalarray=np.asarray(zvalList).astype(np.float)
    wvalarray=np.asarray(wvalList).astype(np.float)


    ones=np.ones(xvalarray.shape)
    x=np.array([xvalarray]).T

    regr=linear_model.LinearRegression()
    regr.fit(x,yvalarray)

    currGradRate=regr.predict(2016)
    predGradRate=regr.predict(2020)

    ones=np.ones(xvalarray.shape)
    x=np.array([xvalarray]).T

    regr=linear_model.LinearRegression()
    regr.fit(x,zvalarray)

    currPopRate=regr.predict(2016)
    predPopRate=regr.predict(2020)

    ones = np.ones(xvalarray.shape)
    x = np.array([xvalarray]).T

    regr = linear_model.LinearRegression()
    regr.fit(x, wvalarray)

    currIncRate = regr.predict(2016)
    predIncRate = regr.predict(2020)

    newylist=[]
    for document in cursor:
        newylist.append(document)

    newyarray=np.asarray(newylist).astype(np.float)
    x1valarray=np.asarray(xvalarray).astype(np.float)
    x2valarray=np.asarray(yvalarray).astype(np.float)
    x3valarray=np.asarray(zvalarray).astype(np.float)
    x4valarray = np.asarray(wvalarray).astype(np.float)

    ones=np.ones(x1valarray.shape)
    x=np.array([x1valarray,x2valarray,x3valarray,x4valarray]).T
    regr=linear_model.LinearRegression()
    regr.fit(x,newyarray)


    a=regr.coef_
    CurrTotalCrime=(a[0]*2016)+(a[1]*currGradRate)+ (a[2]*currPopRate)+(a[3]*currIncRate)+regr.intercept_
    PredTotalCrime=(a[0]*2020)+(a[1]*predGradRate)+(a[2]*predPopRate)+(a[3]*predIncRate)+regr.intercept_
    cur=[]
    cur.append(float(CurrTotalCrime))
    pred=[]
    pred.append(float(PredTotalCrime))

    db.minorcrimeCurr.insert({"zipcode": index, "current": cur})
    db.minorcrimePred.insert({"zipcode": index, "predict": pred})
    print(index)
    print("Current " , CurrTotalCrime)
    print("Prediction ", PredTotalCrime)
