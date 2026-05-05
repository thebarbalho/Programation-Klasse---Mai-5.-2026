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
ufs = st.multiselect("Selecione o estado (UF):", df["uf"].unique())
sexo = st.selectbox("Selecione o sexo:", ["Todos", "M", "F"])

df_filtrado = df.copy()
if nome:
    df_filtrado = df_filtrado[df_filtrado["nome"].str.contains(nome, case=False)]

if partidos:
    df_filtrado = df_filtrado[df_filtrado["partido"].isin(partidos)]

if ufs:
    df_filtrado = df_filtrado[df_filtrado["uf"].isin(ufs)]

if sexo != "Todos":
    df_filtrado = df_filtrado[df_filtrado["sexo"] == sexo]

st.write(f"Resultados encontrados: {len(df_filtrado)}")
st.dataframe(df_filtrado)

# COMPARAÇÃO DE DEPUTADOS FEDERAIS
st.title('COMPARAÇÃO DE DEPUTADOS FEDERAIS')

st.subheader("Lista de Deputados")

st.dataframe(df_filtrado[["nome", "partido", "uf", "sexo"]])

if len(comparar) > 5:
    st.warning("Selecione no máximo 5 deputados.")
else:
    df_comparacao = df[df["nome"].isin(comparar)]

    if len(comparar) >= 2:
        colunas = st.columns(len(comparar))

        for i, nome_dep in enumerate(comparar):
            deputado = df[df["nome"] == nome_dep].iloc[0]

            with colunas[i]:
                st.subheader(nome_dep)
                st.write(f"**Partido:** {deputado['partido']}")
                st.write(f"**UF:** {deputado['uf']}")
                st.write(f"**Sexo:** {deputado['sexo']}")

        st.subheader("Comparação geral")
