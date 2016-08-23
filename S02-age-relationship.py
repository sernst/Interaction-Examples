import pandas as pd
import cauldron as cd
import numpy as np
from cauldron import plotting
import plotly.graph_objs as go

df = cd.shared.df  # type: pd.DataFrame
AGE_RANGE = cd.shared.AGE_RANGE

df_yes = df[df.dress_code == 1]
df_no = df[df.dress_code == 0]

params = np.polyfit(
    df_yes['average_age'].values,
    df_yes['daily_revenue'].values,
    1
)

traces_yes = [
    go.Scatter(
        x=df_yes.average_age,
        y=df_yes.daily_revenue,
        name='Tie Dye',
        mode='markers',
        marker={'color': plotting.get_color(0, 0.25)}
    ),
    go.Scatter(
        x=AGE_RANGE,
        y=[params[0] * age + params[1] for age in AGE_RANGE],
        name='Tie Dye',
        mode='lines',
        line={'color': plotting.get_color(0), 'width': 5}
    )
]

params = np.polyfit(
    df_no['average_age'].values,
    df_no['daily_revenue'].values,
    1
)

traces_no = [
    go.Scatter(
        x=df_no.average_age,
        y=df_no.daily_revenue,
        name='Solid',
        mode='markers',
        marker={'color': plotting.get_color(3, 0.25)}
    ),
    go.Scatter(
        x=AGE_RANGE,
        y=[params[0] * age + params[1] for age in AGE_RANGE],
        name='Solid',
        mode='lines',
        line={'color': plotting.get_color(3), 'width': 5}
    )
]

traces_compare = [
    traces_no[-1],
    traces_yes[-1]
]

cd.display.plotly(
    data=traces_no,
    layout=plotting.create_layout(
        {'showlegend': False},
        'Daily Revenue Versus Average Age (Solid Polo)',
        'Average Age (Years)',
        'Daily Revenue ($k)'
    )
)

y_min = min(df_yes['daily_revenue'].min(), df_no['daily_revenue'].min())
y_max = min(df_yes['daily_revenue'].max(), df_no['daily_revenue'].max())

cd.display.plotly(
    data=traces_yes,
    layout=plotting.create_layout(
        {'showlegend': False},
        'Daily Revenue Versus Average Age (Tie-Dye Polo)',
        'Average Age (Years)',
        'Daily Revenue ($k)'
    )
)

cd.display.plotly(
    data=traces_compare,
    layout=plotting.create_layout(
        {'showlegend': True},
        'Daily Revenue Versus Average Age',
        'Average Age (Years)',
        'Daily Revenue ($k)',
        y_bounds=[y_min, y_max]
    )
)


