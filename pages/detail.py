import streamlit as st
import utils
import streamlit_pydantic as sp

# hide pages sidebar
st.set_page_config(initial_sidebar_state="collapsed")

@st.cache_resource
def load_data():
    return utils.load_data()


def _parse_selected_id():
    params = st.experimental_get_query_params()
    if 'id' not in params:
        return None
    
    selected_record_id_text = params['id'][0]
    try:
        return int(selected_record_id_text)
    except ValueError:
        return None


st.markdown(
    "<a href='/'>Back</a>",
    unsafe_allow_html=True
)

df = load_data()
selected_id = _parse_selected_id()
if selected_id not in df.index:
    st.write("n/a")
else:
    record = df.loc[selected_id]
    selected =  utils.CatModel.from_df_record(record)
    st.image(selected.img_uri)
    data = sp.pydantic_form(key="my_form", model=selected) 
    if data and selected_id in df.index:
        df.loc[selected_id] = data.dict() 
        utils.save_data(df)


    
