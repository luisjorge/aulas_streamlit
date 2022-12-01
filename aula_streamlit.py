import streamlit as st
st.write("Bem vindo à nossa primeira aplicação streamlit na UC Ánálise e Visualização de Dados")

# Texto
st.title ("isto é o título da aplicação")
st.header("isto é o cabeçalho")
st.subheader("isto é o subcabeçalho")
st.markdown("isto é markdown")
st.caption("isto é a legenda")
st.code(" x=2021") #Isto é código
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

#Input 1
st.checkbox('sim')
st.button('Clicar')
st.radio('Indique o seu género:',['Masculino','Feminino'])
st.selectbox('Selecione o seu género:',['Masculino','Feminino'])
st.multiselect('Escolha um planeta:',['Jupiter', 'Marte', 'Neptuno'])
st.select_slider('Selecione uma nota:', ['Mau', 'Bom', 'Excelente'])
st.slider('Escolha um número:', 0,50)
st.number_input('Escolha um número:', 0,10)
st.text_input('Email:')
st.date_input('Data de viagem:')
st.time_input('Horário de escola:')
st.text_area('Descrição:')
st.file_uploader('Carregue uma fotografia:')
st.color_picker('Escolha a sua cor favorita:')

#Vídeos, audio e imagem
st.image("dados_adicionais_aula/FC_Porto.png", width=400, caption="O maior clube do Mundo!")
st.audio("dados_adicionais_aula/hino.mp3")
st.video("dados_adicionais_aula/jogo.mp4")

#Gráficos

import plotly.express as px
import pandas as pd

centro=pd.read_csv("dados_adicionais_aula/datacentro.csv",sep=";", decimal=",")
fig = px.scatter(centro, x="Famílias clássicas_2021", y="Índice de dependência2021",
           color="concelhos_nutiii", size="População residente estimada_2021",
           marginal_x="box")
st.plotly_chart(fig, use_container_width=True)
