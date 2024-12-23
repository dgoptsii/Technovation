import streamlit as st 
import page1
import page2
import page3
import page4


#dictionary (key, value)
PAGES = {
    "Page 1": page1,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4
}

st.sidebar.title('My Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()