import streamlit as st

user_name = st.session_state.get('user_name')

if user_name:
    st.markdown("# Welcome, " + user_name + " ❄️")
else:
    st.markdown("# Welcome! ❄️")
