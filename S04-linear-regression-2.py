import cauldron as cd
import pandas as pd
from statsmodels import api as sm

df = cd.shared.df  # type: pd.DataFrame

combined = df['average_age'] * df['dress_code']

y = df['daily_revenue'].values

df = pd.DataFrame({
    'average_age': df['average_age'],
    'dress_code': df['dress_code'],
    'int_age_dress': combined
})

x = sm.add_constant(df)
results = sm.OLS(y, x).fit()

print(results.summary())
