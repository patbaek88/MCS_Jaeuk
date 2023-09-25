import pandas as pd
import streamlit as st
from sklearn.decomposition import PCA

st.title('Manufacturing Classification System')  # 타이틀명 지정
st.write('1. Please select FT4 features for PCA in the multi selectbox below') 
multi_select = st.multiselect(
    'Recommendation: SE, CBD, AE, CPS, PD, 9UYS, 9FF, WFA',
    ['BFE', 'SI', 'FRI', 'SE', 'CBD', 'AE', 'AR', 'NAS', 'CPS', 'PD', '9COH', '9UYS', '9MPS', '9FF', '9AIF', '6COH',
     '6UYS', '6MPS', '6FF', '6AIF', 'WFA'],
    default=['SE', 'CBD', 'AE', 'CPS', 'PD', '9UYS', '9FF', 'WFA'])
#st.write('You selected:', multi_select)

st.write('FT4 features')
ft4_features = 'FT4_features.csv'
df_ft4_features = pd.read_csv(ft4_features)
st.write(df_ft4_features)

# loading dataset
filename = 'FT4_DB_Sep2023.csv'

# creating data frame for pandas
df = pd.read_csv(filename)
df = df.set_index('Material')

# df_filtered = df.drop(['Function', 'Project','BFE', 'SI', 'FRI', 'AR', 'NAS', '9COH', '9MPS', '9AIF', '6COH', '6UYS', '6MPS', '6FF', '6AIF'], axis=1)
df_filtered = df[multi_select]

from sklearn.preprocessing import StandardScaler

x = df_filtered.values  # 독립변인들의 value값만 추출
y = df['Function'].values  # 종속변인 추출

x = StandardScaler().fit_transform(x)  # x객체에 x를 표준화한 데이터를 저장

# all features = ['BFE', 'SI', 'FRI', 'SE', 'CBD', 'AE', 'AR', 'NAS', 'CPS', 'PD', '9COH', '9UYS', '9MPS', '9FF', '9AIF', '6COH', '6UYS', '6MPS', '6FF', '6AIF', 'WFA']
features = df_filtered.columns
z = pd.DataFrame(x, columns=features)

pca = PCA(n_components=4)  # 주성분을 몇개로 할지 결정
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents, index=df.index, columns=['pc1', 'pc2', 'pc3', 'pc4'])
# 주성분으로 이루어진 데이터 프레임 구성
pca_explained_variance_ratio = pd.DataFrame(data=pca.explained_variance_ratio_,
                                            index=['Principal Component 1', 'Principal Component 2',
                                                   'Principal Component 3', 'Principal Component 4'],
                                            columns=['Explained Variance Ratio'])
st.write('PCA result based on seleced features')
st.write(pca_explained_variance_ratio)

principalDf["Function"] = df['Function']
principalDf_WG = principalDf[(principalDf['Function'] == 'Filler_WG')]

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

df_pc1_score = df["PC1_score"]

st.write(df_pc1_score)
st.write("Class 1 : Direct Compression,   PC1 score < " + critical_value_class1_1)
st.write("Class 2 : Dry Granulation,        PC1 score < " + critical_value_class3_1)
st.write("Class 3 : Wet Granulation,       PC1 score < " + critical_value_class4_1)
st.write("Class 4 : Other Technology,   PC1 score >= " + critical_value_class4_1)
st.write("")
st.write("")
st.write("")
st.write("2. Please enter formulation information below")
API_df = df[(df['Function']=='API')]
API_list = API_df.index.to_list()
API_name = st.selectbox('Select API', API_list)

API_content = st.text_input('API_content (%)')

Excipient_1_name = st.selectbox(
    'Select Excipient_1',
    ("Lactose DCL-15 (Supertab 30GR)_1", "Lactose DCL-15 (Supertab 30GR)_2", "Lactose monohydrate (Supertab 30GR)_1",
     "Lactose monohydrate (Supertab 30GR)_2", "Lactose #200", "Lactose monohydrate (Tablettose 80)_1",
     "Lactose monohydrate (Tablettose 80)_2", "Lactose monohydrate (FLOWLAC 90)", "Lactose Anhydrous (Supertab 21AN)",
     "Lactose Anhydrous (Supertab 22AN)", "Lactose Anhydrous (21AN)", "D-Mannitol", "Pearlitol 100 SD",
     "Pearlitol 160 C", "Pearlitol 200 SD_1", "Pearlitol 200 SD_2", "Parteck Delta M", "Parteck M 100", "Vivapur 301",
     "Vivapur 112", "Vivapur 302", "Vivapur 12_1", "Vivapur 12_2", "Vivapur 12_3", "Vivapur 200", "Heweten 101_1",
     "Heweten 101_2", "Heweten 101_3", "Heweten 102_1", "Heweten 102_2", "Avicel PH-102", "Avicel PH-200", "DCP D/T_1",
     "DCP D/T_2", "Starch 1500 (Partially pregelatinized maize starch)_1",
     "Starch 1500 (Partially pregelatinized maize starch)_2", "Startab (Directly compressible starch)_1",
     "Startab (Directly compressible starch)_2", "Starcap 1500",
     "CELLACTOSE 80 (75% Lactose monohydrate+25% Cellulose powdered)", "Prosolv SMCC 50_1", "Prosolv SMCC 50_2",
     "Prosolv SMCC HD90", "Prosolv Easytab SP LM", "Kollidon VA 64 (Copovidone)_1", "Kollidon VA 64 (Copovidone)_2",
     "Kollidon 12 PF (Povidone)_1", "Kollidon 12 PF (Povidone)_2", "Kollidon 12 PF (Povidone)_3",
     "Kollidon 30 (Povidone)", "Methocel E6 (Methocel E6 PREMIUM LV HPMC)",
     "Methocel E15 (Methocel E15 PREMIUM LV HPMC)_1", "Methocel E15 (Methocel E15 PREMIUM LV HPMC)_2",
     "Methocel K15M (Methocel E15 PREMIUM CR HPMC)", "HPMC E5LV (Hypromellose 2910)", "CMC Sodium_CMC 7L2P",
     "CMC Sodium_CMC 7MF PH BET", "EXPLOSOL", "Kollidon CL (Crospovidone)", "Ac-Di-Sol SD-711_1", "Ac-Di-Sol SD-711_2",
     "Vivasol_1", "Vivasol_2"))

Excipient_1_content = st.text_input('Excipient_1_content (%)')

Excipient_2_name = st.selectbox(
    'Select Excipient_2',
    ("Lactose DCL-15 (Supertab 30GR)_1", "Lactose DCL-15 (Supertab 30GR)_2", "Lactose monohydrate (Supertab 30GR)_1",
     "Lactose monohydrate (Supertab 30GR)_2", "Lactose #200", "Lactose monohydrate (Tablettose 80)_1",
     "Lactose monohydrate (Tablettose 80)_2", "Lactose monohydrate (FLOWLAC 90)", "Lactose Anhydrous (Supertab 21AN)",
     "Lactose Anhydrous (Supertab 22AN)", "Lactose Anhydrous (21AN)", "D-Mannitol", "Pearlitol 100 SD",
     "Pearlitol 160 C", "Pearlitol 200 SD_1", "Pearlitol 200 SD_2", "Parteck Delta M", "Parteck M 100", "Vivapur 301",
     "Vivapur 112", "Vivapur 302", "Vivapur 12_1", "Vivapur 12_2", "Vivapur 12_3", "Vivapur 200", "Heweten 101_1",
     "Heweten 101_2", "Heweten 101_3", "Heweten 102_1", "Heweten 102_2", "Avicel PH-102", "Avicel PH-200", "DCP D/T_1",
     "DCP D/T_2", "Starch 1500 (Partially pregelatinized maize starch)_1",
     "Starch 1500 (Partially pregelatinized maize starch)_2", "Startab (Directly compressible starch)_1",
     "Startab (Directly compressible starch)_2", "Starcap 1500",
     "CELLACTOSE 80 (75% Lactose monohydrate+25% Cellulose powdered)", "Prosolv SMCC 50_1", "Prosolv SMCC 50_2",
     "Prosolv SMCC HD90", "Prosolv Easytab SP LM", "Kollidon VA 64 (Copovidone)_1", "Kollidon VA 64 (Copovidone)_2",
     "Kollidon 12 PF (Povidone)_1", "Kollidon 12 PF (Povidone)_2", "Kollidon 12 PF (Povidone)_3",
     "Kollidon 30 (Povidone)", "Methocel E6 (Methocel E6 PREMIUM LV HPMC)",
     "Methocel E15 (Methocel E15 PREMIUM LV HPMC)_1", "Methocel E15 (Methocel E15 PREMIUM LV HPMC)_2",
     "Methocel K15M (Methocel E15 PREMIUM CR HPMC)", "HPMC E5LV (Hypromellose 2910)", "CMC Sodium_CMC 7L2P",
     "CMC Sodium_CMC 7MF PH BET", "EXPLOSOL", "Kollidon CL (Crospovidone)", "Ac-Di-Sol SD-711_1", "Ac-Di-Sol SD-711_2",
     "Vivasol_1", "Vivasol_2"))

Excipient_2_content = st.text_input('Excipient_2_content (%)')

Excipient_3_name = st.selectbox(
    'Select Excipient_3',
    ("Lactose DCL-15 (Supertab 30GR)_1", "Lactose DCL-15 (Supertab 30GR)_2", "Lactose monohydrate (Supertab 30GR)_1",
     "Lactose monohydrate (Supertab 30GR)_2", "Lactose #200", "Lactose monohydrate (Tablettose 80)_1",
     "Lactose monohydrate (Tablettose 80)_2", "Lactose monohydrate (FLOWLAC 90)", "Lactose Anhydrous (Supertab 21AN)",
     "Lactose Anhydrous (Supertab 22AN)", "Lactose Anhydrous (21AN)", "D-Mannitol", "Pearlitol 100 SD",
     "Pearlitol 160 C", "Pearlitol 200 SD_1", "Pearlitol 200 SD_2", "Parteck Delta M", "Parteck M 100", "Vivapur 301",
     "Vivapur 112", "Vivapur 302", "Vivapur 12_1", "Vivapur 12_2", "Vivapur 12_3", "Vivapur 200", "Heweten 101_1",
     "Heweten 101_2", "Heweten 101_3", "Heweten 102_1", "Heweten 102_2", "Avicel PH-102", "Avicel PH-200", "DCP D/T_1",
     "DCP D/T_2", "Starch 1500 (Partially pregelatinized maize starch)_1",
     "Starch 1500 (Partially pregelatinized maize starch)_2", "Startab (Directly compressible starch)_1",
     "Startab (Directly compressible starch)_2", "Starcap 1500",
     "CELLACTOSE 80 (75% Lactose monohydrate+25% Cellulose powdered)", "Prosolv SMCC 50_1", "Prosolv SMCC 50_2",
     "Prosolv SMCC HD90", "Prosolv Easytab SP LM", "Kollidon VA 64 (Copovidone)_1", "Kollidon VA 64 (Copovidone)_2",
     "Kollidon 12 PF (Povidone)_1", "Kollidon 12 PF (Povidone)_2", "Kollidon 12 PF (Povidone)_3",
     "Kollidon 30 (Povidone)", "Methocel E6 (Methocel E6 PREMIUM LV HPMC)",
     "Methocel E15 (Methocel E15 PREMIUM LV HPMC)_1", "Methocel E15 (Methocel E15 PREMIUM LV HPMC)_2",
     "Methocel K15M (Methocel E15 PREMIUM CR HPMC)", "HPMC E5LV (Hypromellose 2910)", "CMC Sodium_CMC 7L2P",
     "CMC Sodium_CMC 7MF PH BET", "EXPLOSOL", "Kollidon CL (Crospovidone)", "Ac-Di-Sol SD-711_1", "Ac-Di-Sol SD-711_2",
     "Vivasol_1", "Vivasol_2"))

Excipient_3_content = st.text_input('Excipient_3_content (%)')

Excipient_4_name = st.selectbox(
    'Select Excipient_4',
    ("Lactose DCL-15 (Supertab 30GR)_1", "Lactose DCL-15 (Supertab 30GR)_2", "Lactose monohydrate (Supertab 30GR)_1",
     "Lactose monohydrate (Supertab 30GR)_2", "Lactose #200", "Lactose monohydrate (Tablettose 80)_1",
     "Lactose monohydrate (Tablettose 80)_2", "Lactose monohydrate (FLOWLAC 90)", "Lactose Anhydrous (Supertab 21AN)",
     "Lactose Anhydrous (Supertab 22AN)", "Lactose Anhydrous (21AN)", "D-Mannitol", "Pearlitol 100 SD",
     "Pearlitol 160 C", "Pearlitol 200 SD_1", "Pearlitol 200 SD_2", "Parteck Delta M", "Parteck M 100", "Vivapur 301",
     "Vivapur 112", "Vivapur 302", "Vivapur 12_1", "Vivapur 12_2", "Vivapur 12_3", "Vivapur 200", "Heweten 101_1",
     "Heweten 101_2", "Heweten 101_3", "Heweten 102_1", "Heweten 102_2", "Avicel PH-102", "Avicel PH-200", "DCP D/T_1",
     "DCP D/T_2", "Starch 1500 (Partially pregelatinized maize starch)_1",
     "Starch 1500 (Partially pregelatinized maize starch)_2", "Startab (Directly compressible starch)_1",
     "Startab (Directly compressible starch)_2", "Starcap 1500",
     "CELLACTOSE 80 (75% Lactose monohydrate+25% Cellulose powdered)", "Prosolv SMCC 50_1", "Prosolv SMCC 50_2",
     "Prosolv SMCC HD90", "Prosolv Easytab SP LM", "Kollidon VA 64 (Copovidone)_1", "Kollidon VA 64 (Copovidone)_2",
     "Kollidon 12 PF (Povidone)_1", "Kollidon 12 PF (Povidone)_2", "Kollidon 12 PF (Povidone)_3",
     "Kollidon 30 (Povidone)", "Methocel E6 (Methocel E6 PREMIUM LV HPMC)",
     "Methocel E15 (Methocel E15 PREMIUM LV HPMC)_1", "Methocel E15 (Methocel E15 PREMIUM LV HPMC)_2",
     "Methocel K15M (Methocel E15 PREMIUM CR HPMC)", "HPMC E5LV (Hypromellose 2910)", "CMC Sodium_CMC 7L2P",
     "CMC Sodium_CMC 7MF PH BET", "EXPLOSOL", "Kollidon CL (Crospovidone)", "Ac-Di-Sol SD-711_1", "Ac-Di-Sol SD-711_2",
     "Vivasol_1", "Vivasol_2"))

Excipient_4_content = st.text_input('Excipient_4_content (%)')

## Buttons
if st.button("Calculate"):
    API_content_f = float(API_content)
    Excipient_1_content_f = float(Excipient_1_content)
    Excipient_2_content_f = float(Excipient_2_content)
    Excipient_3_content_f = float(Excipient_3_content)
    Excipient_4_content_f = float(Excipient_4_content)

    API_PC1_score = df.loc[API_name]["PC1_score"]
    Excipient_1_PC1_score = df.loc[Excipient_1_name]["PC1_score"]
    Excipient_2_PC1_score = df.loc[Excipient_2_name]["PC1_score"]
    Excipient_3_PC1_score = df.loc[Excipient_3_name]["PC1_score"]
    Excipient_4_PC1_score = df.loc[Excipient_4_name]["PC1_score"]
    API_PC1_score_1 = str(round(API_PC1_score, 3))
    Excipient_1_PC1_score_1 = str(round(Excipient_1_PC1_score, 3))
    Excipient_2_PC1_score_1 = str(round(Excipient_2_PC1_score, 3))
    Excipient_3_PC1_score_1 = str(round(Excipient_3_PC1_score, 3))
    Excipient_4_PC1_score_1 = str(round(Excipient_4_PC1_score, 3))

    # Total_amount = API_amount + Excipient1_amount + Excipient2_amount + Excipient3_amount

    Mixture_PC1_score = API_PC1_score * API_content_f / 100 + Excipient_1_PC1_score * Excipient_1_content_f / 100 + Excipient_2_PC1_score * Excipient_2_content_f / 100 + Excipient_3_PC1_score * Excipient_3_content_f / 100 + Excipient_4_PC1_score * Excipient_4_content_f / 100
    Mixture_PC1_score_1 = str(round(Mixture_PC1_score, 3))


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


    MCS = func(Mixture_PC1_score)

    st.write("Mixture PC1 score = " + Mixture_PC1_score_1)
    st.write("Mixture MCS result = " + MCS)
    st.write("------------------------Calculation Detail------------------------")
    st.write("API PC1 score = " + API_PC1_score_1 + " / content = " + API_content + " %")
    st.write("Excipient_1 PC1 score = " + Excipient_1_PC1_score_1 + " / content = " + Excipient_1_content + " %")
    st.write("Excipient_2 PC1 score = " + Excipient_2_PC1_score_1 + " / content = " + Excipient_2_content + " %")
    st.write("Excipient_3 PC1 score = " + Excipient_3_PC1_score_1 + " / content = " + Excipient_3_content + " %")
    st.write("Excipient_4 PC1 score = " + Excipient_4_PC1_score_1 + " / content = " + Excipient_4_content + " %")
    st.write("Mixture PC1 score = " + Mixture_PC1_score_1)
    st.write("Class 1 : Direct Compression,   PC1 score < " + critical_value_class1_1)
    st.write("Class 2 : Dry Granulation,        PC1 score < " + critical_value_class3_1)
    st.write("Class 3 : Wet Granulation,       PC1 score < " + critical_value_class4_1)
    st.write("Class 4 : Other Technology,   PC1 score >= " + critical_value_class4_1)
