import streamlit as st
import pandas as pd
import numpy as np
st.title('Titulo del proyecto')
st.write('12345')
click=st.button('click')
activated=st.toggle("activar")
number=st.slider("Elige un número", 0, 3600)
st.write("El número es: ",number) 
