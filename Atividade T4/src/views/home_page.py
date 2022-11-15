import streamlit as st


def home_page():
    home, produtos, carrinho = st.tabs(["Home", "Produtos", "Carrinho"])
    

    with home:
        st.title("Bem vindo a lohjinha da Mel")
        st.image('assets/mel_1.jpeg')
        st.subheader("Aqui você poderá encontrar varias fotos da salsicha mais carismática do Brasil")


    with produtos:
        st.title("Produtos")
         col1, col2, col3 = st.columns(3)