from pymongo import MongoClient
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D

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

cursor=db.total_crime.find({"zipcode":10006}).distinct("tc")
cursor1=db.total_crime.find({"zipcode":10006}).distinct("year")
cursor2=db.total_crime.find({"zipcode":10006}).distinct("gradrate")
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

xvaltrain=xvalarray[:10]
xvaltest=xvalarray[10]

xval1train=xval1array[:10]
xval1test=xval1array[10]

yvaltrain=y[:10]
yvaltest=y[10]



ones=np.ones(xvaltrain.shape)
x=np.array([xvaltrain,xval1train]).T
ones1=np.ones(xvaltest.shape)
x1=np.array([xvaltest,xval1test]).T

regr=linear_model.LinearRegression()
regr.fit(x,yvaltrain)



print("10013")
print(regr.coef_)
print(regr.intercept_)

def plot_figs(fig_num, elev, azim, x, clf):
    fig = plt.figure(fig_num, figsize=(4, 3))
    plt.clf()
    ax = Axes3D(fig, elev=elev, azim=azim)

    ax.scatter(x[:, 0], x[:, 1], yvaltrain, c='k', marker='+')
    ax.plot_surface(np.array([[-.1, -.1], [.15, .15]]),
                    np.array([[-.1, .15], [-.1, .15]]),
                    clf.predict(np.array([[-.1, -.1, .15, .15],
                                          [-.1, .15, -.1, .15]]).T
                                ).reshape((2, 2)),
                    alpha=.5)
    ax.set_xlabel('X_1')
    ax.set_ylabel('X_2')
    ax.set_zlabel('Y')
    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])

#Generate the three different figures from different views
elev = 43.5
azim = -110
plot_figs(1, elev, azim, x, regr)

elev = -.5
azim = 0
plot_figs(2, elev, azim,x, regr)

elev = -.5
azim = 90
plot_figs(3, elev, azim, x, regr)

plt.show()






