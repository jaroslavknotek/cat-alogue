import utils, time
import pandas as pd
from pydantic import HttpUrl
import httpx

import streamlit as st 
from utils import CatModel 

# HOME page with a list of cats

# hide pages sidebar
st.set_page_config(initial_sidebar_state="collapsed")

def load_data():
    return utils.load_data()

def create_row(row,record):
    
    col1,col2 = st.columns(2)
    with col1:
        clickable_image = f"""
        <a href="/detail?id={record.Index}" target="_blank">  
            <img src="{record.img_uri}" style="width:100%;"> 
        </a>"""
        # st.image(record.img_uri)
        st.markdown(clickable_image,unsafe_allow_html=True)
    with col2:
        st.header(record.name)
        st.write(record.sex)
        st.write(record.age)
        
def delete_cat(df, record):
    df = df[df.index != record.Index]
    df = df.reset_index(drop=True)
    st.success("Cat deleted successfully!")
    utils.save_data(df)
    return df

def custom_write_df(df):
    for record in df.itertuples():
        with st.container():
            row = st.columns(1)
            minus = st.empty()
            if minus.button(":heavy_minus_sign:", key=record):
                delete_cat(df, record)
                minus.empty()
                continue
            create_row(row,record)
    return df

def is_valid_url(url):
    try:
        response = httpx.head(url)
        return response.status_code == 200
    except httpx.HTTPError:
        return False

def submitted():
    st.session_state.submitted = True
def reset():
    st.session_state.submitted = False
    
# Read cats' data
df = load_data()
query = st.text_input("Search")

if st.button(":heavy_plus_sign:"):
    with st.form(key="add_cat_form"):
        name = st.text_input("Name", key="name")
        sex = st.text_input("Sex", key="sex")
        age = st.number_input("Age", key="age")
        image = st.text_input("URL Image", key="image")
        st.form_submit_button(label="Add Cat", on_click=submitted)
        
if st.session_state.get('submitted', False):
    try:
        if is_valid_url(st.session_state.image):
            cat = CatModel(name=st.session_state.name, sex=st.session_state.sex, age=float(st.session_state.age), img_uri=HttpUrl(st.session_state.image))
            df = utils.drop_concatenated(df)
            df.loc[len(df.index)] = [cat.name, cat.sex, cat.age, cat.img_uri]
            df = utils.concatenated_column(df)
            success = st.success("New cat added successfully!")
            utils.save_data(df)
        else:
            st.error("Invalid URL. Please provide a valid URL for the image.")
    except: 
        st.error("Something went wrong.")
    reset()

if query is None or query.strip() == "":
    # print all cats
    df = custom_write_df(df)
else:
    # print filtered cats only 
    df_filtered = utils.search_all(df,query)
    custom_write_df(df_filtered)
