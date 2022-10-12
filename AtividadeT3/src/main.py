import streamlit as st
import views.login as log
import views.home_page as home

if 'pagina' not in st.session_state:
    st.session_state.pagina = 'logar'

if st.session_state.pagina == 'logar':
    log.show_login_page()
    
if st.session_state.pagina == 'home':
    home.show_home_page()

