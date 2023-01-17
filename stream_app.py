from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from vega_datasets import data


"""
# Welcome to Chris Franklin's StreamLit Web App for Deploying DataScience Projects!
This is inspired from the StreamLit.io site.
See the website for more info https://streamlit.io/

My name is Chris Franklin. I work in data science on several data science projects.  
I have completed projects in web-scraping, sentiment analysis, time-series, nlp, robotics with python and data visualizations of all types. 
I also cheerfully volunteer doing data science mentoring. 

Below is my Twitter Web-Scraping Sentiment Analysis Project using Google Colab. Run the code by signing into a gmail account. 
I will be deploying my Twitter Sentiment Analysis Project on Streamlit in the future :)

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


alt.themes.enable("streamlit")

@st.experimental_memo
def get_data():
    source = data.stocks()
    source = source[source.date.gt("2004-01-01")]
    return source

source = get_data()

# Original time series chart. Omitted `get_chart` for clarity
chart = get_chart(source)

# Input annotations
ANNOTATIONS = [
    ("Mar 01, 2008", "Pretty good day for GOOG"),
    ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"),
    ("Nov 01, 2008", "Market starts again thanks to..."),
    ("Dec 01, 2009", "Small crash for GOOG after..."),
]

# Create a chart with annotations
annotations_df = pd.DataFrame(ANNOTATIONS, columns=["date", "event"])
annotations_df.date = pd.to_datetime(annotations_df.date)
annotations_df["y"] = 0
annotation_layer = (
    alt.Chart(annotations_df)
    .mark_text(size=15, text="IBM", dx=9, dy=-10, align="center")
    .encode(
        x="date:T",
        y=alt.Y("y:Q"),
        tooltip=["event"],
    )
    .interactive()
)

# Display both charts together
st.altair_chart((chart + annotation_layer).interactive(), use_container_width=True)
