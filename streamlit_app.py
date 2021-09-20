from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

import os

def file_selector(folder_path='./data'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)


@st.cache
def load_data(data):
    return pd.read_csv(data)

filename = file_selector()
st.write(f'is csv: {filename.endswith(".csv")}')
df = load_data(filename)

# @st.cache  # 👈 This function will be cached
# def my_slow_function(arg1, arg2):
#     # Do something really slow in here!
#     return the_output

st.write('You selected `%s`' % filename)
st.write(df.head(20))
st.write(df.shape)
st.echo(df.dtypes)

"""
### remove unused columns
"""


def intersection(l1, l2):  # get_diff_list
    set_difference = set(l1) - set(l2)

    list_difference = list(set_difference)
    return list_difference


st.code("""def intersection(l1, l2): #get_diff_list
        set_difference = set(l1) - set(l2)

        list_difference = list(set_difference)
        return list_difference""")

st.code("""df = df.drop(columns=intersection(all_columns, features_category))""")

all_columns = df.columns

features_category = ["AF3", "F7", "F3", "F5", "T7", "P7", "O1", "O2", "P8", "T8", "FC6", "F4", "F8", "AF4", "EventId"]

df = df.drop(columns=intersection(all_columns, features_category))
st.dataframe(df)
