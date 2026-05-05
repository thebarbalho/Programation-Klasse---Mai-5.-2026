import streamlit as st
import pandas as pd

st.title('DEPUTADOS FEDERAIS - 2022')
st.image('https://www.brasildefato.com.br/wp-content/uploads/2024/10/image_processing20200201-29235-11htggk.jpg')
df = pd.read_csv('deputados_2022.csv')
st.dataframe(df)
