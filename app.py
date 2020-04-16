import os
import pandas as pd
import plotly.express as px
import plotly.io as pio
import streamlit as st


# consts
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# data
df = pd.read_csv(
    "{APP_ROOT}/data/data.csv".format(APP_ROOT=APP_ROOT),
)

# style
st.markdown(
    """
    <style>.reportview-container .main .block-container{padding: 0}</style>
    """,
    unsafe_allow_html=True
)

# sidemenu
st.sidebar.markdown(
    "### MLB Draft: Pick-By-Pick Bonuses"
)
year = st.sidebar.selectbox(
    "Year", df["Year"].sort_values().unique()
)
team = st.sidebar.selectbox(
    "Team", df["TeamNm"].sort_values().unique()
)
template = st.sidebar.selectbox(
    "Template", list(pio.templates.keys())
)

# body
st.markdown(
    "# {year}/{team}".format(year=year, team=team)
)
ydf = df[df["Year"] == year]
tdf = ydf[ydf["TeamNm"] == team]
graph = px.line(
    tdf, x='Pick', y='BonusAmount', color='BonusType',
    template=template, hover_name='FullNm', height=500, width=800,
    labels=dict({"BonusAmount": "$", "Pick": "Overall Pick"})
)
graph.update_layout(
    margin=dict(l=20, r=20, t=50, b=0),
)
st.write(graph)