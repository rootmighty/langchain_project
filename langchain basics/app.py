import langchain_helper
import streamlit as st
st.set_page_config(page_title="LangChain Helper", page_icon=":robot:")

st.title("Restaurant Recommendation")
with st.sidebar:
    cuisine = st.selectbox("Pick a cuisine", ("Indian", "Italian", "Mexican", "Arabic"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine=cuisine)

    st.header(response["restaurant_name"].strip())
    st.write(
        "**Menu Items**"
    )
    menu_items = response["food_items"].strip().split(",")

    for item in menu_items:
        st.write("-", item)