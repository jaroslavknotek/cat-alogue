import utils

import streamlit as st 

@st.cache_data
def load_data():
    return utils.load_data()


def custom_write_df(df):
    for row in df.itertuples():

        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.image(row.img_uri)
            with col2:
                st.header(row.name)
                st.write(row.sex)
                st.write(row.age)


df = load_data()

query = st.text_input("Search")

if query is None or query.strip() == "":
    custom_write_df(df)
else:
    df_filtered = utils.search_all(df,query)
    custom_write_df(df_filtered)
