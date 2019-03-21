import matplotlib.pyplot as pl
import pandas as pd
cement=pd.read_csv("C:/Users/yammu/Downloads/yamm.csv")
cement.plot.scatter("x2","y")
cement.plot("y")

import matplotlib.pyplot as plt
import matplotlib.image as mping
import numpy as np
img=mping.imread("C:/Users/yammu/Downloads/ll_13367751.jpg")
imgplot=plt.imshow(img)


import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('ggplot')
data = np.random.randn(50)
print(plt.style.available)

import pandas as pd
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,25,23,34,40,30,25,46])}
df = pd.DataFrame(d,'Name','Age')
print(df.mode())



















