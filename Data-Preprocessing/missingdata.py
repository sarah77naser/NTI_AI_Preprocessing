import numpy as np
from sklearn.impute import SimpleImputer

#
#
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')

data=[[12,np.nan,34],[10,3,np.nan],[np.nan,11,20]]
print("Original Data : \n",data)

imputer=imputer.fit(data)
data=imputer.transform(data)
print("Imputed Data \n:",data)