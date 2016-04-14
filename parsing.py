from pymongo import MongoClient
import matplotlib as plt
import numpy as np
from sklearn import linear_model


client=MongoClient()
db=client.zipwatch
cursor=db.total_crime.find({}).distinct("tc")
cursor1=db.total_crime.find({}).distinct("year")
cursor2=db.total_crime.find({}).distinct("gradrate")
yvalList=[]
xvalList=[]
xvalList1=[]
finalxList=[]


yvalList=cursor



xvalList=cursor1


xvalList1=cursor2

xvalarray=np.asarray(xvalList)
y=np.asarray(yvalList)
xval1array=np.asarray(xvalList1)

ones=np.ones(xvalarray.shape)
x=np.array([xvalarray,xval1array]).T

regr=linear_model.LinearRegression()
regr.fit(x,y)
print(regr.coef_)
















