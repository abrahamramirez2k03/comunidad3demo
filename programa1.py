import streamlit as st
import pandas as pd
import numpy as np
st.title('Titulo del najsdfjknasdf')
st.write('12345')
click=st.button('click')
activated=st.toggle("activar")
number=st.slider("Elige un número", 0, 3600)
st.write("El número es: ",number) 
n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)

choice=st.number_input("Elige un número: ", 1, 31)
