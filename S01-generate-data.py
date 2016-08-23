import os
import random

import pandas as pd
import cauldron as cd

STORE_COUNT = 400
MIN_AGE = 21
MAX_AGE = 58

cd.shared.AGE_RANGE = [MIN_AGE, MAX_AGE]

store_data = []


def create_row():
    """
    Creates a store data row
    :return:
    """

    dress_code = random.randint(1, 4) > 2
    average_age = random.uniform(MIN_AGE, MAX_AGE)
    daily_revenue = random.gauss(100, 30)

    if dress_code:
        age_factor = (average_age - MIN_AGE) / (MAX_AGE - MIN_AGE)
        age_factor = (age_factor - 0.4) / 0.8
        daily_revenue += random.gauss(
            age_factor * 0.7 * daily_revenue,
            0.05 * daily_revenue
        )

    return dict(
        id=len(store_data) + 1,
        dress_code=1 if dress_code else 0,
        average_age=average_age,
        daily_revenue=float(round(daily_revenue)),
    )

if os.path.exists('store_data.csv'):
    df = pd.read_csv('store_data.csv')
else:
    while len(store_data) < STORE_COUNT:
        store_data.append(create_row())
    df = pd.DataFrame(store_data)
    df.to_csv('store_data.csv')

cd.display.table(df)
cd.shared.df = df

