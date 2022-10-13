import streamlit as st

def show_home_page():
   main, produtos, carrinho = st.tabs(['Home', 'Produtos', 'Carrinho'])

   with main:
      st.title("Bem vindo a lohjinha da Mel")
      st.image('assets/mel_1.jpeg')
      st.write("Aqui você poderá encontrar varias fotos da salsicha mais carismática do Brasil")
      

   with produtos:
      col1, col2, col3 = st.columns(3)
      
      with col1:
         st.image('assets/Mel_HotDog.jpeg')
         st.write('Mel com skin de Hot-Dog')
         st.write('R$10.000')
         st.button(label='Adicionar ao carrinho', help = 'clique para adicionar')

      