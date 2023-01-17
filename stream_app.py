from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Chris Franklin's StreamLit Web App for Deploying DataScience Projects!
This is inspired from the StreamLit.io site.
See the website for more info https://streamlit.io/

My name is Chris Franklin. I work in data science on several data science projects.  
I have completed projects in web-scraping, sentiment analysis, time-series, nlp, robotics with python and data visualizations of all types. 
I also cheerfully volunteer doing data science mentoring. 

Below is my Twitter Web-Scraping Sentiment Analysis Project using Google Colab. Run the code by signing into a gmail account. 
I will be deploying my Twitter Sentiment Analysis Project on Streamlit in the future:)

https://colab.research.google.com/drive/16ILWejhcam279Aetc8QGanhyeuSPIbQA


StreamLit.io content example from their website


StreamLit Documentation below:

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
    
st.write("Streamlit Play:) creating dataframes and plotly plots")

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))


  

st.dataframe(df)  # Same as st.write(df)

lst = [['Geek', 25], ['is', 30], 
       ['for', 26], ['Geeksforgeeks', 22]] 

# creating df object with columns specified    
df2 = pd.DataFrame(lst, columns =['Tag', 'number']) 

df2.plot()

st.dataframe(df2)  # Same as st.write(df)


#another dataframe https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart
df3 = px.data.gapminder()

fig = px.scatter(
    df3.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)

st.dataframe(df3)
