import streamlit as st
from src.controllers.item_controller import ItemController


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
        def add_on_cart(item):
            st.session_state.cart.append(item)

        with col1:
            item1= ItemController().get_by_id(2)
            st.image('assets/mel_com_capa_de_chuva.jpeg')
            st.subheader(item1.name)
            st.write(item1.price)
            st.write(item1.description)
            st.button(label='Adicionar ao carrinho', help='Clique para adicionar ao carrinho', on_click=add_on_cart(item1),key=item1.id) 

        with col2:
            item2= ItemController().get_by_id(3)
            st.image('assets/Mel_HotDog.jpeg')
            st.subheader(item2.name)
            st.write(item2.price)
            st.write(item2.description)
            st.button(label='Adicionar ao carrinho', help='Clique para adicionar ao carrinho', on_click=add_on_cart(item2),key=item2.id)

        with col3:
            item3= ItemController().get_by_id(4)
            st.image('assets/Mel_Cone.jpeg')
            st.subheader(item3.name)
            st.write(item3.price)
            st.write(item3.description)
            st.button(label='Adicionar ao carrinho', help='Clique para adicionar ao carrinho', on_click=add_on_cart(item3),key=item3.id)


    with carrinho:
        st.title("Carrinho")

        for item in st.session_state.cart:
            with st.container():
                st.write(item.name)
                st.write(item.price)
                st.write(item.description)