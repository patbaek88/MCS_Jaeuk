import streamlit as st
import pandas as pd

st.title('Manfacturing Classification System')  # 타이틀명 지정

st.write('Set API Name and Conent(%) to Get Formulation Recommendation')
link1 = '[Formulation Recommendation](http://mcs-jaeuk-recommendation.streamlit.app)'
st.markdown(link1, unsafe_allow_html=True)
st.write("")
st.write("")
st.write('Design Your Formulation and Check Manufacturing Class')
link2 = '[Formulation Design](http://mcs-jaeuk-design.streamlit.app)'
st.markdown(link2, unsafe_allow_html=True)
st.write("")
st.write("")
st.write('Current FT4 Data Base')
database = 'Excipients_APIs_DB_Feb2023.csv'
df_database = pd.read_csv(database)
st.write(df_database)
st.write('FT4 Features')
ft4_features = 'FT4_features.csv'
df_ft4_features = pd.read_csv(ft4_features)
st.write(df_ft4_features)
