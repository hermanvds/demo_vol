import pandas
import numpy

# pandas DF
df = pandas.read_csv('CME_ATM_VolCube_20200610.csv')
df

# numpy array
numpy_array = df.to_numpy()
numpy_array