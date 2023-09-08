import streamlit as st
import pandas as pd

st.title('Manufacturing Classification System')  # 타이틀명 지정
st.write("")
st.write("Formulation and Manufacturing Class Recommendation Based on API and Its Content(%)")
link1 = '[Formulation Recommendation](http://mcs-jaeuk-recommendation.streamlit.app)'
st.markdown(link1, unsafe_allow_html=True)
st.write("")
st.write("")
st.write("Manufacturing Class Recommendation for User-Designed Formulation")
link2 = '[Formulation Design](http://mcs-jaeuk-design.streamlit.app)'
st.markdown(link2, unsafe_allow_html=True)
st.write("")
st.write("")


#multiple_files = st.file_uploader('CSV',type="csv", accept_multiple_files=True)
#for file in multiple_files:
#	dataframe = pd.read_csv(file)
#	file.seek(0)
#	st.write(dataframe)

database = 'FT4_DB_Feb2023.csv'
df_database = pd.read_csv(database)
ft4_features = 'FT4_features.csv'
df_ft4_features = pd.read_csv(ft4_features)
st.write('FT4 Data Base ('+database+')')
st.write(df_database)
st.write('FT4 Features')
st.write(df_ft4_features)
