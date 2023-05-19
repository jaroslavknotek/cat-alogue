import utils

import streamlit as st 

# HOME page with a list of cats

# hide pages sidebar
st.set_page_config(initial_sidebar_state="collapsed")

@st.cache_data
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

def custom_write_df(df):
    for record in df.itertuples():
        with st.container():
            row = st.columns(1)
            create_row(row,record)


# Read cats' data
df = load_data()
query = st.text_input("Search")

if query is None or query.strip() == "":
    # print all cats
    custom_write_df(df)
else:
    # print filtered cats only 
    df_filtered = utils.search_all(df,query)
    custom_write_df(df_filtered)
