import plotly.figure_factory as ff
import pandas as pd
import plotly.express as px 

df=pd.read_csv("data.csv")

fig=ff.create_distplot([df["Avg Rating"]],["Avg Rating"])

fig.show()

# Such a Small code took si=o much Time LOL
