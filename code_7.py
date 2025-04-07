import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
#If any of this libraries is missing from your computer. Please install them using pip.

filename = 'Flight_Delays_2018.csv'
df=pd.read_csv('Flight_Delays_2018.csv')

#describedata =df[['ARR_DELAY', 'DEP_DELAY', 'CARRIER_DELAY', 'DISTANCE']].describe()
#print(describedata)

y = df['ARR_DELAY']
x = df['DEP_DELAY']

x = sm.add_constant(x)

model = sm.OLS(y, x).fit()

print(model.summary())
#ARR_DELAY is the column name that should be used as dependent variable (Y).

#box plot

plt.scatter(df['DEP_DELAY'], df['ARR_DELAY'])  
plt.title('Arrival Delay vs. Departure Delay')
plt.xlabel('Depature Delay (minutes)')
plt.ylabel('Arrival Delay (minutes)')
plt.show()