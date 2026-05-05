import streamlit as st
import pandas as pd

# INTERFACE NO STREAMLIT
st.title('DEPUTADOS FEDERAIS - 2022')
st.image('https://www.brasildefato.com.br/wp-content/uploads/2024/10/image_processing20200201-29235-11htggk.jpg')
df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)

# PROCURA POR DEPUTADOS FEDERAIS
st.title('SEARCH DE DEPUTADOS FEDERAIS - 2022')
nome = st.text_input("Digite o nome do deputado:")
partidos = st.multiselect("Selecione o partido:", df["partido"].unique())
uf = st.multiselect("Selecione o estado (UF):", df["uf"].unique())
sexo = st.selectbox("Selecione o sexo:", ["Todos", "M", "F"])

df_filtrado = df.copy()
if nome:
    df_filtrado = df_filtrado[df_filtrado["nome"].str.contains(nome, case=False)]

if partidos:
    df_filtrado = df_filtrado[df_filtrado["partido"].isin(partidos)]

if uf:
    df_filtrado = df_filtrado[df_filtrado["uf"].isin(ufs)]

if sexo != "Todos":
    df_filtrado = df_filtrado[df_filtrado["sexo"] == sexo]

st.write(f"Resultados encontrados: {len(df_filtrado)}")
st.dataframe(df_filtrado)

# COMPARAÇÃO DE DEPUTADOS FEDERAIS
st.title('COMPARAÇÃO DE DEPUTADOS FEDERAIS')

deputado1_name = st.selectbox("Deputado 1", list(deputados.keys()))
deputado2_name = st.selectbox("Deputado 2", list(deputados.keys()))

if st.button("Comparar deputados"):

  if deputado1_name == deputado2_name:        
        st.warning("Escolha deputados diferentes!")    
  else:        
        deputado1 = deputados[deputado1_name]        
        deputado2 = deputados[deputado2_name]   
