import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/aryan/Desktop/coding/Coding (Phython)/Graphs/CovidInfo.csv")

fig = px.scatter(df, x="date", y="cases",title='Covid Data')
fig.show()