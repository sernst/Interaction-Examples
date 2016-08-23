import cauldron as cd
from cauldron import plotting
import plotly.graph_objs as go

df = cd.shared.df

cd.display.plotly(
    data=go.Histogram(
        x=df['average_age']
    ),
    layout=plotting.create_layout(
        {'showlegend': False},
        'Distribution of Average Ages for Stores',
        'Average Age (#)',
        'Store Frequency (#)'
    )
)

cd.display.plotly(
    data=go.Histogram(
        x=df['daily_revenue']
    ),
    layout=plotting.create_layout(
        {'showlegend': False},
        'Distribution of Average Revenue for Stores',
        'Daily Revenue ($)',
        'Store Frequency (#)'
    )
)
