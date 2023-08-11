import streamlit as st

st.title('Manfacturing Classification System')  # 타이틀명 지정

st.write('Set API Name and Conent(%) to Get Formulation Recommendation')
link1 = '[Formulation Recommendation](http://mcs-jaeuk-recommendation.streamlit.app)'
st.markdown(link1<br>, unsafe_allow_html=True)

st.write('Design Formulations and Check Manufacturing Class')
link2 = '[Formulation Design](http://mcs-jaeuk-design.streamlit.app)'
st.markdown(link2, unsafe_allow_html=True)


