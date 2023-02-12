import streamlit as st
import mysql.connector as connection
import pandas as pd
import plotly.express as px


col1, col2, col3 = st.columns(3)

with col1:
    st.image('https://download.logo.wine/logo/PhonePe/PhonePe-Logo.wine.png', width=150)
with col2:
    st.title("Phone Pulse Data")
with col3:
    pass

col4, col5 = st.columns(2)

with col4:
    option1 = st.selectbox("Select Year", ("2018", "2019", "2020", "2021", "2022"))
with col5:
    option2 = st.selectbox("Users or Transactions", ("Users", "Transactions"))


db_connection = connection.connect(host="localhost", database='PhonePe', user="root", password="Ferrari488Pi!")
db_cursor = db_connection.cursor()
db_cursor.execute('SELECT * FROM test')
table_rows = db_cursor.fetchall()
df = pd.DataFrame(table_rows)

df.to_csv("test.csv", header=['state', 'users'])

df = pd.read_csv("test.csv")

fig = px.choropleth(
    df,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='state',
    color='users',
    color_continuous_scale='Blues'
)

fig.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig, use_container_width=True)
