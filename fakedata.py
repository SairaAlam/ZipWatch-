from pymongo import MongoClient
import matplotlib as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
client=MongoClient()
db=client.zipwatch

zipcodelist=[10013,10004,10006,10282,10038,10002,10003,10009,10011,10010,10001,10016,10022,10019, 10036, 10021, 10065
              ]

zip=[10128, 10023, 10024, 10029, 10025, 10035, 10027, 10026, 10031, 10030, 10039, 10032,
     10040, 10454, 10455, 10459, 10451, 10462, 10472, 10473, 10456, 10468, 10466, 10475, 10457, 10460, 10469, 10461,
     10461
     ]

zipt=[
    10463, 10467, 10458, 11224, 11229, 11235, 11214, 11210, 11204, 11219, 11203, 11226, 11209, 11220, 11236, 11230,
    11225, 11212, 11233, 11208, 11207, 11239, 11231, 11213, 11217, 11215, 11216, 11221

    ]

zipa=[ 11237, 11201, 11205, 11238, 11211, 11206, 11222, 11694, 11691, 11418, 11416, 11432, 11451, 11385, 11426, 11694,
        11691, 11418, 11416, 11432, 11451, 11385, 11426,
        11427, 11411, 11413, 11417, 11365, 11366, 11367, 11101, 11354, 11355, 11368, 11373, 11364, 11361, 11375, 11412

        ]

zipb=[11434, 11436,
      11103, 11106, 10312, 10304, 10306, 10301
      ]
scale=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 1,
       4, 1, 3, 4, 4, 5, 5, 2, 4, 1, 1, 1, 2,
       1, 4, 5, 1, 1, 2, 2, 3, 1, 5, 1, 5, 1, 1, 1, 1,
       1,3, 1, 2, 4, 1, 5, 4, 1,4, 1, 3, 1, 1, 1, 1, 1,
    5, 2, 3, 1, 1, 1, 1, 3,1, 5, 1,1
    , 1,1, 5, 1, 1, 1, 1, 4, 1, 1, 1, 2, 1, 5, 1, 4,
       1, 1, 1, 2, 1, 5, 1,
       1, 1, 3, 1, 5, 1, 1, 1, 4, 5, 1, 3, 4, 1,5,2,
       4, 1,3, 1, 2, 4, 1, 3
       ]






for index in zipcodelist:
        db.fakedata.insert({"zipcode":index,"rate":1})

for index1 in zip:
    db.fakedata.insert({"zipcode":index1,"rate":2})

for index2 in zipt:
    db.fakedata.insert({"zipcode":index2,"rate":3})

for index3 in zipa:
    db.fakedata.insert({"zipcode":index3,"rate":4})

for index4 in zipb:
    db.fakedata.insert({"zipcode":index4,"rate":5})