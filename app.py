import streamlit as st
import numpy as np
import pandas as pd
import time 
import plotly.express as px


#read csv from a github repo https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv
dados = pd.read_csv("bank.csv")


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://www.google.com",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('Real-Time / Live Data Science Dashboard')

# st.write(dados.head())


job_filter = st.selectbox("Select the Job", pd.unique(dados['job']))

#Creating a single-element container.
placeholder = st.empty()


#Dataframe filter
dados = dados[dados['job'] == job_filter]

# near real-time / live feed simulation 
while True:
# for seconds in range(200):

    dados['age_new'] = dados['age'] * np.random.choice(range(1,5))
    dados['balance_new'] = dados['balance'] * np.random.choice(range(1,5))

    # creating KPIs 
    avg_age = np.mean(dados['age_new'])
    count_married = int(dados[dados['marital'] == 'married']['marital'].count() + np.random.choice(range(1,30)))
    
    balance = np.mean(dados['balance_new'])

    with placeholder.container():
        # Creating three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(label="Age", value=round(avg_age), delta=round(avg_age) -12)
        kpi2.metric(label="Married Count", value=int(count_married), delta= -10 + count_married)
        kpi3.metric(label="A/C Balance $", value=f"$ {round(balance,2)}", delta= - round(balance))
        

        # Create two columns for charts
        col1,col2 = st.columns(2)

        with col1:
            st.markdown('### First Chart')
            fig = px.density_heatmap(
                data_frame=dados,
                y = "age_new",
                x = "marital"
            )
            st.write(fig)
        with col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(
                data_frame=dados,
                x = 'age_new'
            )
            st.write(fig2)

        st.markdown(" ### Detailed View")
        st.dataframe(dados)
        time.sleep(0.5)


