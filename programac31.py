import streamlit as st
import pandas as pd
import numpy as np
st.title('Titulo del proyecto')
st.write('12345')
click=st.button('click')
activated=st.toggle("activar")
number=st.slider("Elige un número", 0, 3600)
df = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
