import pandas as pd
import streamlit as st
import numpy as np
#import matplotlib.pyplot as plt

# Give the page an h1 title
st.title('Uber Pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# It takes a fairly long amount of time to load data and
# we wouldn't want to reload everytime the app is updated
# You can avoid this by caching data with @st.cache
# Although there are limitations. Read limitations here
#[Limitations to st.cache](https://docs.streamlit.io/library/get-started/create-an-app)


@st.cache
def load_data(nrows):
    """
    Load nrows of data
    :param nrows:
    :return: data
    """
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Letting user know data is loading
data_load_state = st.text('Loading data...')
# Load 100 rows of data
data = load_data(10000)
# Notify user that the data has loaded successfully
data_load_state.text('Done! using st.cache...done!')

# The table section
st.subheader('Raw data')
st.write(data)

# Drawing a bar chart
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=25, range=(0,24))[0]
st.bar_chart(hist_values)

st.subheader('Map of all pickups')

#st.map(data)
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.subheader('Raw data')
st.write(data)
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


