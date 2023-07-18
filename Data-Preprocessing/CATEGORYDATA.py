"""# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 
# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.NaN, strategy = 'mean')
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Encoding categorical data
# Encoding the Independent varialble
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([("country",OneHotEncoder(),[0])], remainder= "")
X = ct.fit_transform(X)
x = pd.DataFrame(X)
LabelEncoder_X = LabelEncoder()
X[:,0] = LabelEncoder_X.fit_transform(X[:,0])
x = pd.DataFrame(X)
onehotencoder = OneHotEncoder()
X = onehotencoder.fit_transform(X).toarray()
x = pd.DataFrame(X)


x_1 = X[:,1:]

LabelEncoder_y =LabelEncoder()
y =LabelEncoder_y.fit_transform(y)
"""
""
# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([('Country', OneHotEncoder(),[0])], remainder="passthrough")
X=ct.fit_transform(X)
x=pd.DataFrame(X)
