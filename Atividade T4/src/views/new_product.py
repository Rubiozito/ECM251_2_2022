import streamlit as st
from src.controllers.item_controller import ItemController
from src.models.item import Item

def new_product_page():
    st.title("Cadastrar novo produto")
    st.write("Preencha os campos abaixo para cadastrar um novo produto")
    
    st.write("id do produto:")
    id = st.text_input(label='id do produto:', placeholder = 'id do produto')

    st.write("Nome do produto:")
    name = st.text_input(label='Digite o nome do produto:', placeholder = 'Nome do produto📦')

    st.write("Descrição do produto:")
    description = st.text_input(label='Digite a descrição do produto:', placeholder = 'Descrição do produto📝')

    st.write("Preço do produto:")
    price = st.number_input(label='Digite o preço do produto:', min_value=1.0, max_value=100000.0, step=0.5)

    new_item = Item(id, name, description, price)

    def cadastrar_novo_produto():
        if(id != '' and name != '' and description != '' and price != ''):
            ItemController().create_item(new_item)
            st.success('Produto cadastrado com sucesso')
        else:
            st.error('Digite todos os campos')

    st.button(label='Cadastrar', help='Clique para cadastrar', on_click=cadastrar_novo_produto)

    def go_to_home():
        st.session_state.page = 'home'

    st.button(label='Voltar', help='Clique para voltar', on_click=go_to_home)