import cauldron as cd
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = cd.shared.df  # type: pd.DataFrame

combined = df['average_age'] * df['dress_code']

x = np.array([
    df['average_age'].values,
    df['dress_code'].values,
    combined
])
x = np.transpose(x)

y = df['daily_revenue'].values
y = np.transpose(y)

model = LinearRegression().fit(x, y)

# The coefficients
print('Coefficients: \n', model.coef_)

# The mean square error
print(
    "Residual sum of squares: %.2f" % np.mean((model.predict(x) - y) ** 2)
)
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % model.score(x, y))

