import pandas as pd
import streamlit as st
from sklearn.decomposition import PCA

st.title('Manfacturing Classification System')  # 타이틀명 지정

# loading dataset
filename = 'Excipients_APIs_DB_Feb2023.csv'

# creating data frame for pandas
df = pd.read_csv(filename)
df = df.set_index('Material')

df_filtered = df.drop(['Classification', 'Project','BFE', 'SI', 'FRI', 'AR', 'NAS', '9COH', '9MPS', '9AIF', '6COH', '6UYS', '6MPS', '6FF', '6AIF'], axis=1)

from sklearn.preprocessing import StandardScaler

x = df_filtered.values  # 독립변인들의 value값만 추출
y = df['Classification'].values  # 종속변인 추출

x = StandardScaler().fit_transform(x)  # x객체에 x를 표준화한 데이터를 저장

# all features = ['BFE', 'SI', 'FRI', 'SE', 'CBD', 'AE', 'AR', 'NAS', 'CPS', 'PD', '9COH', '9UYS', '9MPS', '9FF', '9AIF', '6COH', '6UYS', '6MPS', '6FF', '6AIF', 'WFA']
features = df_filtered.columns
z = pd.DataFrame(x, columns=features)

pca = PCA(n_components=4)  # 주성분을 몇개로 할지 결정
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents, index=df.index, columns=['pc1', 'pc2', 'pc3', 'pc4'])
# 주성분으로 이루어진 데이터 프레임 구성

principalDf["Classification"] = df['Classification']
principalDf_WG = principalDf[(principalDf['Classification'] == 'Filler_WG')]

critical_value_WG_min = principalDf_WG['pc1'].min()
critical_value_WG_max = principalDf_WG['pc1'].max()
pc1_min = principalDf['pc1'].min()

df["PC1"] = principalDf['pc1']
df["PC1_score"] = df['PC1'] - pc1_min

critical_value_class1 = (-pc1_min + critical_value_WG_min) - (critical_value_WG_max - critical_value_WG_min) * 0.1
critical_value_class2 = (-pc1_min + critical_value_WG_min)
critical_value_class3 = (-pc1_min + critical_value_WG_min) + (critical_value_WG_max - critical_value_WG_min) * 0.1
critical_value_class4 = (-pc1_min + critical_value_WG_max)

critical_value_class1_1 = str(round(critical_value_class1, 3))
critical_value_class2_1 = str(round(critical_value_class2, 3))
critical_value_class3_1 = str(round(critical_value_class3, 3))
critical_value_class4_1 = str(round(critical_value_class4, 3))


API_name = st.selectbox(
    'Select API',
    ("CS-BT-077", "DIN-juyeol91-094", "21ET70-1", "GQ72-bckim-160-14", "GPR-LSE-144", "GPR-LSE-108",
     "22GQ72-1", "Gemif_B200519031", "Gemif_B210520041", "Gemig_DPS21010", "Gemig_A211206027",
     "Gemig_A211227003", "Gemig_B201217124", "Gemig_B201217125", "Gemig_B210112096", "Gemig_A211220029",
     "Gemig_A211217014", "Gemig_A211222018", "Gemig_B201217128", "Gemig_A211223004", "Ler_Y210402006",
     "Ler_Y200226018", "Ler_Y201124042", "Ler_A210729008", "Ler_A210924002", "MCR-jinokham-081", "19MC72-1",
     "Met_Y201109028", "Met_Y201109026", "Met_Y201109027", "Met_A211109009", "Met_Y201127008",
     "Met_A211204008", "Met_Y201127011", "Met_Y201127010", "Met_Y201127004", "Rosu_A211027004",
     "Rosu_A210826001", "TTB-jungmins87-022_formA", "TT-01025-CL", "21NT70-1_formB", "Val_B201013040",
     "Val_B201217126", "Val_B201013041", "Val_B201013042", "Val_A211216009", "11GD70-1", "GDB20002",
     "20GD70-1", "GDB2003", "GDB20001"))

API_content = st.text_input('API_content (%)')

## Buttons
if st.button("Recommend"):
    API_content_f = float(API_content)
    API_PC1_score = df.loc[API_name]["PC1_score"]
    API_PC1_score_1 = str(round(API_PC1_score, 3))

    # DC1_formulation
    DC1_Excipient1_name = "Heweten 102_1"
    DC1_Excipient1_PC1_score = df.loc[DC1_Excipient1_name]["PC1_score"]
    DC1_Excipient1_PC1_score_1 = str(round(DC1_Excipient1_PC1_score, 3))
    DC1_Excipient1_content = 100 - 5 - 3 - API_content_f
    DC1_Excipient1_content_1 = str(DC1_Excipient1_content)

    DC1_Excipient2_name = "Vivasol_1"
    DC1_Excipient2_PC1_score = df.loc[DC1_Excipient2_name]["PC1_score"]
    DC1_Excipient2_PC1_score_1 = str(round(DC1_Excipient2_PC1_score, 3))
    DC1_Excipient2_content = 5
    DC1_Excipient2_content_1 = str(DC1_Excipient2_content)

    DC1_Excipient3_name = "PRUV"
    DC1_Excipient3_PC1_score = 0
    DC1_Excipient3_PC1_score_1 = str(DC1_Excipient3_PC1_score)
    DC1_Excipient3_content = 3
    DC1_Excipient3_content_1 = str(DC1_Excipient3_content)

    # DC2_formulation
    DC2_Excipient1_name = "Prosolv SMCC HD90"
    DC2_Excipient1_PC1_score = df.loc[DC2_Excipient1_name]["PC1_score"]
    DC2_Excipient1_PC1_score_1 = str(round(DC2_Excipient1_PC1_score, 3))
    DC2_Excipient1_content = 100 - 20 - 3 - 1 - API_content_f
    DC2_Excipient1_content_1 = str(DC2_Excipient1_content)

    DC2_Excipient2_name = "Lactose monohydrate (Tablettose 80)_1"
    DC2_Excipient2_PC1_score = df.loc[DC2_Excipient2_name]["PC1_score"]
    DC2_Excipient2_PC1_score_1 = str(round(DC2_Excipient2_PC1_score, 3))
    DC2_Excipient2_content = 20
    DC2_Excipient2_content_1 = str(DC2_Excipient2_content)

    DC2_Excipient3_name = "Vivasol_1"
    DC2_Excipient3_PC1_score = df.loc[DC2_Excipient3_name]["PC1_score"]
    DC2_Excipient3_PC1_score_1 = str(round(DC2_Excipient3_PC1_score, 3))
    DC2_Excipient3_content = 3
    DC2_Excipient3_content_1 = str(DC2_Excipient3_content)

    DC2_Excipient4_name = "Smg"
    DC2_Excipient4_PC1_score = 0
    DC2_Excipient4_PC1_score_1 = str(DC2_Excipient4_PC1_score)
    DC2_Excipient4_content = 1
    DC2_Excipient4_content_1 = str(DC2_Excipient4_content)

    # WG1_formulation
    WG1_Excipient1_name = "Heweten 101_1"
    WG1_Excipient1_PC1_score = df.loc[WG1_Excipient1_name]["PC1_score"]
    WG1_Excipient1_PC1_score_1 = str(round(WG1_Excipient1_PC1_score, 3))
    WG1_Excipient1_content = 100 - 8 - 3.5 - 1 - API_content_f
    WG1_Excipient1_content_1 = str(WG1_Excipient1_content)

    WG1_Excipient2_name = "Kollidon 30 (Povidone)"
    WG1_Excipient2_PC1_score = df.loc[WG1_Excipient2_name]["PC1_score"]
    WG1_Excipient2_PC1_score_1 = str(round(WG1_Excipient2_PC1_score, 3))
    WG1_Excipient2_content = 8
    WG1_Excipient2_content_1 = str(WG1_Excipient2_content)

    WG1_Excipient3_name = "Vivasol_1"
    WG1_Excipient3_PC1_score = df.loc[WG1_Excipient3_name]["PC1_score"]
    WG1_Excipient3_PC1_score_1 = str(round(WG1_Excipient3_PC1_score, 3))
    WG1_Excipient3_content = 3.5
    WG1_Excipient3_content_1 = str(WG1_Excipient3_content)

    WG1_Excipient4_name = "Smg"
    WG1_Excipient4_PC1_score = 2
    WG1_Excipient4_PC1_score_1 = str(WG1_Excipient4_PC1_score)
    WG1_Excipient4_content = 1
    WG1_Excipient4_content_1 = str(WG1_Excipient4_content)

    DC1_MCS_score = API_PC1_score * API_content_f / 100 + DC1_Excipient1_PC1_score * DC1_Excipient1_content / 100 + DC1_Excipient2_PC1_score * DC1_Excipient2_content / 100 + DC1_Excipient3_PC1_score * DC1_Excipient3_content / 100
    DC1_MCS_score_1 = str(round(DC1_MCS_score, 3))

    DC2_MCS_score = API_PC1_score * API_content_f / 100 + DC2_Excipient1_PC1_score * DC2_Excipient1_content / 100 + DC2_Excipient2_PC1_score * DC2_Excipient2_content / 100 + DC2_Excipient3_PC1_score * DC2_Excipient3_content / 100 + DC2_Excipient4_PC1_score * DC2_Excipient4_content / 100
    DC2_MCS_score_1 = str(round(DC2_MCS_score, 3))

    WG1_MCS_score = API_PC1_score * API_content_f / 100 + WG1_Excipient1_PC1_score * DC1_Excipient1_content / 100 + WG1_Excipient2_PC1_score * WG1_Excipient2_content / 100 + WG1_Excipient3_PC1_score * WG1_Excipient3_content / 100 + WG1_Excipient4_PC1_score * WG1_Excipient4_content / 100
    WG1_MCS_score_1 = str(round(WG1_MCS_score, 3))

    def func(x):
        if x < critical_value_class1:
            return "Class 1"
        elif x < critical_value_class2:
            return "Class 1/2"
        elif x < critical_value_class3:
            return "Class 2/3"
        elif x <= critical_value_class4:
            return "Class 3"
        else:
            return "Class 4"

    DC1_MCS = func(DC1_MCS_score)
    DC2_MCS = func(DC2_MCS_score)
    WG1_MCS = func(WG1_MCS_score)

    if DC1_MCS == "Class 1":
        Recommanded_Formulation_Name = "DC1_formulation"
        MCS_score = DC1_MCS_score
        MCS_score_1 = str(round(MCS_score, 3))
        MCS_result = "Class 1"
    elif DC1_MCS == "Class 1/2":
        Recommanded_Formulation_Name = "DC1_formulation"
        MCS_score = DC1_MCS_score
        MCS_score_1 = str(round(MCS_score, 3))
        MCS_result = "Class 1/2"
    elif DC2_MCS == "Class 1":
        Recommanded_Formulation_Name = "DC2_formulation"
        MCS_score = DC2_MCS_score
        MCS_score_1 = str(round(MCS_score, 3))
        MCS_result = "Class 1"
    elif DC2_MCS == "Class 1/2":
        Recommanded_Formulation_Name = "DC2_formulation"
        MCS_score = DC2_MCS_score
        MCS_score_1 = str(round(MCS_score, 3))
        MCS_result = "Class 1/2"
    elif WG1_MCS == "Class 2/3":
        Recommanded_Formulation_Name = "WG1_formulation"
        MCS_score = WG1_MCS_score
        MCS_score_1 = str(round(MCS_score, 3))
        MCS_result = "Class 2/3"
    elif WG1_MCS == "Class 3":
        Recommanded_Formulation_Name = "WG1_formulation"
        MCS_score = WG1_MCS_score
        MCS_score_1 = str(round(MCS_score, 3))
        MCS_result = "Class 3"
    else:
        Recommanded_Formulation_Name = "N/A(Other Technology)"
        MCS_score = API_PC1_score
        MCS_score_1 = API_PC1_score_1
        MCS_result = "Class 4"

    if Recommanded_Formulation_Name == "DC1_formulation":
        Excipient1_name = "Heweten 102_1"
        Excipient1_PC1_score = df.loc[Excipient1_name]["PC1_score"]
        Excipient1_PC1_score_1 = str(round(Excipient1_PC1_score, 3))
        Excipient1_content = DC1_Excipient1_content_1
        Excipient1_content_1 = str(Excipient1_content)
        Excipient2_name = "Vivasol_1"
        Excipient2_PC1_score = df.loc[Excipient2_name]["PC1_score"]
        Excipient2_PC1_score_1 = str(round(Excipient2_PC1_score, 3))
        Excipient2_content = 5
        Excipient2_content_1 = str(Excipient2_content)
        Excipient3_name = "PRUV"
        Excipient3_PC1_score = 0
        Excipient3_PC1_score_1 = str(round(Excipient3_PC1_score, 3))
        Excipient3_content = 3
        Excipient3_content_1 = str(Excipient3_content)
        Excipient4_name = "N/A"
        Excipient4_PC1_score = 0
        Excipient4_PC1_score_1 = str(round(Excipient4_PC1_score, 3))
        Excipient4_content = 0
        Excipient4_content_1 = str(Excipient4_content)

    elif Recommanded_Formulation_Name == "DC2_formulation":
        Excipient1_name = "Prosolv SMCC HD90"
        Excipient1_PC1_score = df.loc[Excipient1_name]["PC1_score"]
        Excipient1_PC1_score_1 = str(round(Excipient1_PC1_score, 3))
        Excipient1_content = DC2_Excipient1_content_1
        Excipient1_content_1 = str(Excipient1_content)
        Excipient2_name = "Lactose monohydrate (Tablettose 80)_1"
        Excipient2_PC1_score = df.loc[Excipient2_name]["PC1_score"]
        Excipient2_PC1_score_1 = str(round(Excipient2_PC1_score, 3))
        Excipient2_content = 20
        Excipient2_content_1 = str(Excipient2_content)
        Excipient3_name = "Vivasol_1"
        Excipient3_PC1_score = df.loc[Excipient3_name]["PC1_score"]
        Excipient3_PC1_score_1 = str(round(Excipient3_PC1_score, 3))
        Excipient3_content = 3
        Excipient3_content_1 = str(Excipient3_content)
        Excipient4_name = "Smg"
        Excipient4_PC1_score = 0
        Excipient4_PC1_score_1 = str(round(Excipient4_PC1_score, 3))
        Excipient4_content = 1
        Excipient4_content_1 = str(Excipient4_content)

    elif Recommanded_Formulation_Name == "WG1_formulation":
        Excipient1_name = "Heweten 101_1"
        Excipient1_PC1_score = df.loc[Excipient1_name]["PC1_score"]
        Excipient1_PC1_score_1 = str(round(Excipient1_PC1_score, 3))
        Excipient1_content = WG1_Excipient1_content_1
        Excipient1_content_1 = str(Excipient1_content)
        Excipient2_name = "Kollidon 30 (Povidone)"
        Excipient2_PC1_score = df.loc[Excipient2_name]["PC1_score"]
        Excipient2_PC1_score_1 = str(round(Excipient2_PC1_score, 3))
        Excipient2_content = 8
        Excipient2_content_1 = str(Excipient2_content)
        Excipient3_name = "Vivasol_1"
        Excipient3_PC1_score = df.loc[Excipient3_name]["PC1_score"]
        Excipient3_PC1_score_1 = str(round(Excipient3_PC1_score, 3))
        Excipient3_content = 3.5
        Excipient3_content_1 = str(Excipient3_content)
        Excipient4_name = "Smg"
        Excipient4_PC1_score = 2
        Excipient4_PC1_score_1 = str(round(Excipient4_PC1_score, 3))
        Excipient4_content = 1
        Excipient4_content_1 = str(Excipient4_content)

    else:
        Excipient1_name = "N/A"
        Excipient1_PC1_score = 0
        Excipient1_PC1_score_1 = str(round(Excipient1_PC1_score, 3))
        Excipient1_content = 0
        Excipient1_content_1 = str(Excipient1_content)
        Excipient2_name = "N/A"
        Excipient2_PC1_score = 0
        Excipient2_PC1_score_1 = str(round(Excipient2_PC1_score, 3))
        Excipient2_content = 0
        Excipient2_content_1 = str(Excipient2_content)
        Excipient3_name = "N/A"
        Excipient3_PC1_score = 0
        Excipient3_PC1_score_1 = str(round(Excipient3_PC1_score, 3))
        Excipient3_content = 0
        Excipient3_content_1 = str(Excipient3_content)
        Excipient4_name = "N/A"
        Excipient4_PC1_score = 0
        Excipient4_PC1_score_1 = str(round(Excipient4_PC1_score, 3))
        Excipient4_content = 0
        Excipient4_content_1 = str(Excipient4_content)

    st.write("Recommended Formulation = " +Recommanded_Formulation_Name)
    st.write("Mixture MCS result = "+MCS_result)
    st.write("---------------------Recommended Formulation Detail---------------------")
    st.write("API name / PC1 score / content = "+API_name+" / "+API_PC1_score_1+" / "+API_content+" %")
    st.write("Excipient1 name / PC1 score / content = "+Excipient1_name+" / "+Excipient1_PC1_score_1+" / "+Excipient1_content_1+" % ")
    st.write("Excipient2 name / PC1 score / content = "+Excipient2_name+" / "+Excipient2_PC1_score_1+" / "+Excipient2_content_1+" % ")
    st.write("Excipient3 name / PC1 score / content = "+Excipient3_name+" / "+Excipient3_PC1_score_1+" / "+Excipient3_content_1+" % ")
    st.write("Excipient4 name / PC1 score / content = "+Excipient4_name+" / "+Excipient4_PC1_score_1+" / "+Excipient4_content_1+" % ")
    st.write("Mixture MCS score = " + MCS_score_1)
    st.write("Mixture MCS result = " + MCS_result)
    st.write("Class 1 : Direct Compression,   PC1 score < " + critical_value_class1_1)
    st.write("Class 2 : Dry Granulation,        PC1 score < " + critical_value_class3_1)
    st.write("Class 3 : Wet Granulation,       PC1 score < " + critical_value_class4_1)
    st.write("Class 4 : Other Technology,   PC1 score >= " + critical_value_class4_1)
