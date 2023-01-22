from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
#import plotly as px
#import plotly.figure_factory as ff


"""
# Welcome to Chris Franklin's StreamLit Web App for Deploying DataScience Projects!
This is inspired from the StreamLit.io site.
See the website for more info https://streamlit.io/

My name is Chris Franklin. I work in data science on several data science projects.  
I have completed projects in web-scraping, sentiment analysis, time-series, nlp, robotics with python and data visualizations of all types. 
I also cheerfully volunteer doing data science mentoring. 

My primary programming language for data science projects is Python. 

My Applied Data Science Lab Website is accessible at this url:
https://franklydata.wixsite.com/franklydata

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

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)

# # Add histogram data
# x1 = np.random.randn(200) - 2
# x2 = np.random.randn(200)
# x3 = np.random.randn(200) + 2

# # Group data together
# hist_data = [x1, x2, x3]

# group_labels = ['Group 1', 'Group 2', 'Group 3']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#         hist_data, group_labels, bin_size=[.1, .25, .5])

# # Plot!
# st.plotly_chart(fig, use_container_width=True)

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



