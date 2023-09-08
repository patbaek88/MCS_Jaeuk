import streamlit as st
import pandas as pd

st.title('Manufacturing Classification System')  # 타이틀명 지정
st.write("")
st.write("Formulation And Manufacturing Class Recommendation Based On API And Its Content(%)")
link1 = '[Formulation Recommendation](http://mcs-jaeuk-recommendation.streamlit.app)'
st.markdown(link1, unsafe_allow_html=True)
st.write("")
st.write("")
st.write("Manufacturing Class Recommendation For User-Designed Formulation")
link2 = '[Formulation Design](http://mcs-jaeuk-design.streamlit.app)'
st.markdown(link2, unsafe_allow_html=True)
st.write("")
st.write("")

list_of_names = ['FT4_DB_Feb2023','FT4_features']
dataframes_list = []
for i in range(len(list_of_names)):
    temp_df = pd.read_csv("./csv/"+list_of_names[i]+".csv")
    dataframes_list.append(temp_df)

#database = 'FT4_DB_Feb2023.csv'
#df_database = pd.read_csv(database)
#ft4_features = 'FT4_features.csv'
#df_ft4_features = pd.read_csv(ft4_features)
st.write('FT4 Data Base ('+database+')')
st.write(dataframes_list[0])
st.write('FT4 Features')
#st.write(dataframes_list[1])
