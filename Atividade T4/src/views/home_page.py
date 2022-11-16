import streamlit as st


def home_page():
    home, produtos, carrinho = st.tabs(["Home", "Produtos", "Carrinho"])
    

    with home:
        st.title("Bem vindo a lohjinha da Mel")
        st.image('assets/mel_1.jpeg')
        st.subheader("Aqui você poderá encontrar varias fotos da salsicha mais carismática do Brasil")

        def go_to_edit_user():
            st.session_state.page = 'edit_user'
        def go_to_new_product():
            st.session_state.page = 'new_product'

        st.button(label='Alterar dados', help='Clique para alterar seus dados', on_click=go_to_edit_user)
        st.button(label='Cadastrar produto', help='Clique para cadastrar um novo produto', on_click=go_to_new_product)



    with produtos:
        st.title("Produtos")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.image('assets/mel_com_capa_de_chuva.jpeg')
            st.subheader("Mel com capa de chuva")
            st.write("R$ 10,00")
            st.button("Adicionar ao carrinho")


    with carrinho:
        st.title("Carrinho")