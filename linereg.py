from pymongo import MongoClient
import matplotlib as plt
import numpy as np
from sklearn import linear_model
client=MongoClient()
db=client.zipwatch

ziparray = [10013, 10004, 10006, 10282, 10038,10002, 10003, 10009, 10011,
            10010, 10001, 10016, 10022, 10019, 10036, 10021, 10065,10128,
            None, 10023, 10024, 10029, 10025, 10035, 10027, 10026, 10031, 10030,10039,
            10032, 10033, 10034, 10040, 10454, 10455, 10459, 10474, 10451, 10462, 10472, 10473, 10456,
             10453, 10468, 10466,10475, 10457, 10460, 10469, 10461, 10463, 10467,
            10458, 11224, 11229, 11235, 11214, 11210, 11204, 11219, 11203, 11226, 11209,
            11220,  11236, 11230, 11225, 11212, 11233, 11208, 11207, 11239, 11231, 11213, 11217,
            11215, 11216, 11221, 11237, 11201, 11205, 11238, 11211, 11206, 11222, 11694, 11695,
           11691, 11418, 11416,11423, 11432, 11451, 11385, 11426, 11427, 11411, 11413,
             11417, 11365, 11366, 11367, 11101, 11354, 11355,11359, 11360, 11368,
            11373,  11364, 11361,  11375, 11412, 11434, 11436, 11103,
             11106, 10301,  10302, 10314, 10306,
            10304, 10312]

cursor=db.total_crime.find({"zipcode":10022}).distinct("tc")
cursor1=db.total_crime.find({"zipcode":10022}).distinct("year")
cursor2=db.total_crime.find({"zipcode":10022}).distinct("gradrate")
yvalList=[]
xvalList=[]
xvalList1=[]
finalxList=[]

for document in cursor:
    yvalList.append(document)

for document1 in cursor1:
    xvalList.append(document1)


for document2 in cursor2:
    xvalList1.append(document2)

xvalarray=np.asarray(xvalList)
y=np.asarray(yvalList)
xval1array=np.asarray(xvalList1)

ones=np.ones(xvalarray.shape)
x=np.array([xvalarray,xval1array]).T

regr=linear_model.LinearRegression()
regr.fit(x,y)

print("10022")
print(regr.coef_)
print(regr.intercept_)









