# Data Preprocessing

 

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
## Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler()
#X_train_1 = sc_X.fit_transform(X)
#X_test = sc_X.transform(X_test)
#sc_y = StandardScaler()
#y_train = sc_y.fit_transform(y_train)
## Taking care of missing data   >> imputation 
from sklearn.impute import SimpleImputer #imputation missing data

 
#imputer = SimpleImputer(missing_values = "NaN", strategy = 'mean')
 

from sklearn.preprocessing import Imputer
imputer = SimpleImputer(missing_values = np.NaN, strategy = 'mean')
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

 
import numpy as np
x=pd.DataFrame(X)

"""

# save the imputed data to a new CSV file

df_imputed.to_csv('data_imputed.csv', index=False)

"""