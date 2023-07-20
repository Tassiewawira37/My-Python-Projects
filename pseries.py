import pandas as pd
import matplotlib.pyplot as plt

series = pd.Series([10,20,30,40],['A','B','C','D'])

s1 = pd.Series([1,2,3,4],['a','b','c','d'])
s2 = pd.Series([7,5,1,2],['a','b','c','d'])

def mysquare(x):
    return x**2
print(s1.apply(mysquare))

#when plotting
#for a bar graph ; s1.plot.bar()

s1.plot()
plt.show()
