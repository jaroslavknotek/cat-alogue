import utils

import streamlit as st
# pridala Mary
from streamlit_autorefresh import st_autorefresh

# HOME page with a list of cats

# hide pages sidebar
st.set_page_config(initial_sidebar_state="collapsed")


@st.cache_data
def load_data():
    return utils.load_data()


def create_row(row, record):

    col1, col2 = st.columns(2)
    with col1:
        clickable_image = f"""
        <a href="/detail?id={record.Index}" target="_blank">  
            <img src="{record.img_uri}" style="width:100%;"> 
        </a>"""
        # st.image(record.img_uri)
        st.markdown(clickable_image, unsafe_allow_html=True)
    with col2:
        st.header(record.name)
        st.write(record.sex)
        st.write(record.age)


def custom_write_df(df):
    for record in df.itertuples():
        with st.container():
            row = st.columns(1)
            create_row(row, record)

# MARY`s CHANGES


def open_and_read(path):
    with open(path, mode='r', encoding='utf8') as source:
        my_text = source.read()
    list_text = my_text.split('\n')
    if list_text[-1] == "":
        del list_text[-1]
    # print(list_text, "\n")

    text_list = []
    for el in list_text:
        text_list.append(el.split('\t'))
    # print(text_list, "\n")

    final_list = []
    for el in list_text:
        final_list.append(el.split(','))
    # print(final_list, "\n")

    return final_list


def save_info_list_of_lists(path, result):
    with open(path, mode='w+', encoding='utf8') as result_file:
        for item in result:
            for i in range(len(item)):
                if i != len(item)-1:
                    result_file.write(item[i]+",")
                else:
                    result_file.write(item[i])

            if result.index(item) != len(result)-1:
                result_file.write("\n")


def add_cat(name, sex, age):
    path1 = './data.csv'
    new_list = open_and_read(path1)
    new_list.append([])
    new_list[-1].append(str(int(new_list[-2][0])+1))
    for i in range(3):
        new_list[-1].append(str(float(new_list[-2][0])+1))

    new_list[-1].append(name)
    new_list[-1].append(sex)
    new_list[-1].append(str(float(age)))
    new_list[-1].append('https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg')

    # print(new_list)
    save_info_list_of_lists(path1, new_list)

    df = load_data()


def delete_cat(name, sex, age):
    path1 = './data.csv'
    list_for_delete = open_and_read(path1)
    for i in range(len(list_for_delete)):
        if list_for_delete[i][4] == name and list_for_delete[i][5] == sex and list_for_delete[i][6] == str(float(age)):
            del list_for_delete[i]
            break

    # print(list_for_delete)
    save_info_list_of_lists(path1, list_for_delete)

# * - * - * - * - * - * - * - * - * - * - * - * - * - *


# Read cats' data
df = load_data()
query = st.text_input("Search")

if query is None or query.strip() == "":
    # print all cats
    custom_write_df(df)
else:
    # print filtered cats only
    df_filtered = utils.search_all(df, query)
    custom_write_df(df_filtered)


# Mary`s CHANGES
st.markdown("<h2 style='text-align: center;'>F O R M S </h2>",
            unsafe_allow_html=True)
with st.form("Form 3", clear_on_submit=True):
    st.markdown("<h3 style='text-align: center; color: green'>Add a cat</h3>",
                unsafe_allow_html=True)
    pet_name, pet_sex, pet_age = st.columns(3)
    name = pet_name.text_input("Name")
    sex = pet_sex.text_input("Sex")
    age = pet_age.text_input("Age")
    s_state = st.form_submit_button("Submit")

    if s_state:
        if name == "" or sex == "" or age == "":
            st.warning("Please fill above fields (name, sex, age)!!!")
        # else:
        else:
            st.success("Congr")
            add_cat(name, sex, age)


with st.form("Form 4", clear_on_submit=True):
    st.markdown("<h3 style='text-align: center; color: red'>Delete a cat</h3>",
                unsafe_allow_html=True)
    pet_name, pet_sex, pet_age = st.columns(3)
    name = pet_name.text_input("Name")
    sex = pet_sex.text_input("Sex")
    age = pet_age.text_input("Age")
    print(type(age))
    s_state = st.form_submit_button("Submit")

    if s_state:
        if name == "" or sex == "" or age == "":
            st.warning("Please fill above fields (name, sex, age)!!!")
        else:
            st.success("Congratulation")
            delete_cat(name, sex, age)


st.subheader("Making a button")
ins_cat = st.button("Add a cat")
del_cat = st.button("Delete a cat", disabled=True)
st.write(ins_cat, del_cat)


# Forms, first way to create a form
st.markdown("<h3>Delete a cat (under construction)</h3>",
            unsafe_allow_html=True)
form = st.form("Form 1")
form.text_input("Which cat you want to delete")
form.form_submit_button("Delete the cat")

# Forms, second way to create a form
with st.form("Form 2"):
    st.markdown("<h3>Add a cat (under construction)</h3>",
                unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First name, under construction:")
    l_name = col2.text_input("Last name, under construction")
    st.text_input("Which cat you want to add")
    st.form_submit_button("Add the cat")
