import streamlit as st
from controllers.tarefa_controller import TarefaController

class ListaTarefasView:
    def __init__(self, controller) -> None:
        self.controller = controller 
        self.descricao_tarefa = st.text_input

