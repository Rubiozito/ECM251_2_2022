import streamlit as st

def show_home_page():
   main, produtos, carrinho = st.tabs(['Home', 'Produtos', 'Carrinho'])

   with main:
      st.title("Bem vindo a lohjinha da Mel")
      st.image('assets/mel_1.jpeg')
      st.subheader("Aqui você poderá encontrar varias fotos da salsicha mais carismática do Brasil")
      

   with produtos:
      col1, col2, col3 = st.columns(3)
      
      with col1:
         st.image('assets/Mel_HotDog.jpeg')
         st.write('Mel com skin de Hot-Dog')
         st.subheader('R$10.000')
         st.button(label='Adicionar ao carrinho', help = 'clique para adicionar', key = 1)

      with col2:
         st.image('assets/Mel_com_capa_de_chuva.jpeg')
         st.write('Mel com skin de capa de chuva')
         st.subheader('R$ 4.000')
         st.button(label='Adicionar ao carrinho', help = 'clique para adicionar', key = 2)


      with col3:
         st.image('assets/Mel_Cone.jpeg')
         st.write('Mel com skin de satélite')
         st.subheader('R$5.000')
         st.button(label='Adicionar ao carrinho', help = 'clique para adicionar', key = 3)

   with carrinho:
      st.error("Este carrinho foi perdido enquanto procurava a nota do T2")
      