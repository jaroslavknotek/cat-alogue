import utils

import streamlit as st 

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
    return 
    link = row["Video"].strip()
    evento = row["Evento"].strip()
    if link != "Sin registro":
        image_link = image_dict[evento]
    else:
        image_link = image_dict["Sin registro"]
        clickable_image = f'<img src="{image_link}" style="width:100%;">'
    with c:
        #st.write(clickable_image)
        st.caption(f"{row['Evento'].strip()} - {row['Lugar'].strip()} - {row['Fecha'].strip()} ")
        #st.markdown(f"**{row['Autor'].strip()}**")
        authors_html_list = []
        for author in row["Autor"].split(";"):
            authors_html_list.append(html_link(author, f"/?author={author}", blank=True))
        authors_html = " | ".join(authors_html_list)
        st.markdown(authors_html + clickable_image, unsafe_allow_html=True)
        #st.components.v1.html(authors_html + clickable_image)
        st.markdown(f"{row['Tipo'].strip()}: {row['Titulo'].strip()}")
        


def custom_write_df(df):
    for record in df.itertuples():

        with st.container():
            row = st.columns(1)
            create_row(row,record)


df = load_data()

query = st.text_input("Search")

if query is None or query.strip() == "":
    custom_write_df(df)
else:
    df_filtered = utils.search_all(df,query)
    custom_write_df(df_filtered)
