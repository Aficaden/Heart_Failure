import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.title('CrimeRateRevisited')

st.subheader("Project Objectives/Questions:")
st.markdown("1- Analyze the monthly burglaries and comment your results.")
st.markdown("2- If you are producing a news report and need the average number of burglaries per year, how do you produce the number?")
st.markdown("3- Code the features for spatial lag and time lag.")

st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt



st.subheader("Calls Dataset")
from sqlalchemy import create_engine
engine = create_engine('sqlite:///data/CantonPoliceDept.db')
con = engine.connect()
rs = con.execute("SELECT * FROM Calls")
df_calls = pd.DataFrame(rs.fetchall())
df_calls.columns = rs.keys()
st.dataframe(df_calls)

rs = con.execute("SELECT * FROM Disposition")

df_disp = pd.DataFrame(rs.fetchall())
#create a DataFrame to store the data and fetches all data from the Calls table

df_disp.columns = rs.keys()
#adds column names to df

url1 = 'https://data63206330.file.core.windows.net/data6320/DispositionCategories.csv?sp=rl&st=2021-01-17T14:13:12Z&se=2023-01-18T14:13:00Z&sv=2019-12-12&sig=VLf1FY1jpwbws36%2Birrk%2B2cAyXtyEGO5YQS027DbT8k%3D&sr=f'
df_disp_cat = pd.read_csv(url1, index_col = None, header = 0)
st.dataframe(df_disp_cat)

url2 = 'https://data63206330.file.core.windows.net/data6320/Census_Subzone.csv?sp=rl&st=2021-01-17T14:12:40Z&se=2023-01-18T14:12:00Z&sv=2019-12-12&sig=sOdQ4nJTqYkRKW8%2B32KtoeozTYGmFALwlNpqqJbogGo%3D&sr=f'
df_census = pd.read_csv(url2, index_col = None, header = 0)
st.dataframe(df_census)

url3 = 'https://data63206330.file.core.windows.net/data6320/SubZones_Distance.csv?sp=rl&st=2021-01-17T14:14:05Z&se=2023-01-18T14:14:00Z&sv=2019-12-12&sig=bR1IoPFXSnJwpr%2BMrIw2GBiH1c5zu17gUu5lbaA0GJw%3D&sr=f'
df_spatial = pd.read_csv(url3, index_col = None, header = 0)
st.dataframe(df_spatial)

import datetime as dt
df_calls['Date_Received'] = pd.to_datetime(df_calls['Date_Received'])

df_calls['Day_Name'] = df_calls['Date_Received'].dt.day_name()
df_calls['WEEK'] = df_calls['Date_Received'].dt.isocalendar().week
df_calls['MONTH'] = df_calls['Date_Received'].dt.month
df_calls['YEAR'] = df_calls['Date_Received'].dt.year
df_calls['YEAR_MONTH'] = df_calls['YEAR'].astype(str) + "_" + df_calls['MONTH'].astype(str)
df_calls['SUB_YEAR_MONTH'] = df_calls['YEAR_MONTH'].astype(str) + "_" + df_calls['Subzone'].astype(str)

dummies_D = pd.get_dummies(df_calls['Day_Name'])
dummies_M = pd.get_dummies(df_calls['MONTH'], prefix = 'month')
df_calls = pd.concat([df_calls, dummies_M], axis = 1)
dummies_C = pd.get_dummies(df_calls['Complaint'], prefix = 'call')
df_calls = pd.concat([df_calls, dummies_C], axis = 1)
df_calls = df_calls.drop_duplicates()
st.dataframe(df_calls)

df_calls_month_burg = df_calls[['Subzone', 'Day_Name', 'MONTH', 'YEAR', 'YEAR_MONTH', 'SUB_YEAR_MONTH',
                                'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday','Saturday',
                                'Sunday','call_Burglary']]
year2008 = df_calls_month_burg[(df_calls_month_burg['YEAR'] == 2008)&(df_calls_month_burg['call_Burglary'] == 1)]
year2008_month_burg = year2008.groupby('MONTH')['call_Burglary'].sum().reset_index()
maxMonth = year2008_month_burg.loc[year2008_month_burg['call_Burglary'] ==  year2008_month_burg['call_Burglary'].max(), 'MONTH'].item()
year2008Mmax = year2008[(year2008['MONTH'] == maxMonth)]
day2008Mmax = year2008Mmax.groupby('Day_Name')['call_Burglary'].sum().reset_index().sort_values(by = 'call_Burglary', ascending = False)
sub2008 = year2008Mmax.groupby('Subzone')['call_Burglary'].sum().reset_index()


chart_visual = st.sidebar.selectbox('Select Charts/Plot type',
                                    options= ['Bar Plots', 'Scatterplots', 'Heatmaps'])
st.sidebar.checkbox("Show Analysis by selecting a year", True, key=1)
selected_status1 = st.sidebar.selectbox('Select a year',
                                       options = ['2008', '2009', '2010', '2011', '2012', '2013',
                                                  '2014', '2015', '2016','2017', '2018'])

selected_status2 = st.sidebar.selectbox('Select a month',
                                       options = ['1', '2', '3', '4', '5', '6',
                                                  '7', '8', '9', '10', '11', '12'])



selected_columns = ('creatinine_phosphokinase', 'platelets', 'serum_creatinine',
                    'serum_sodium', 'ejection_fraction', 'anaemia', 'diabetes',
                    'high_blood_pressure', 'smoking','time', 'sex', 'DEATH_EVENT')


if chart_visual == 'Count Plots':
        st.subheader("Plot1: Shows Call Burglaries in different months in 2008")
        if selected_status == '2008':
            fig = plt.figure(figsize=(8, 6))
            sns.countplot(data = year2008_month_burg, x = "MONTH", y = "call_Burglary", palette='deep')
            st.pyplot(fig)

if chart_visual == 'Count Plots':
        st.subheader("Plot2: Shows the number of death based on Gender")
        if selected_status == '2009':
            fig = plt.figure(figsize=(8, 6))
            sns.countplot(x='DEATH_EVENT', data=heart, hue='sex', palette='deep')
            st.pyplot(fig)

if chart_visual == 'Count Plots':
    st.subheader("Plot3: Shows number of death for each age and gender based on selected smoking status")
    input_col, pie_col = st.columns(2)
    if selected_status == '0':
        fig = plt.figure(figsize=(20, 16))
        sns.countplot(data=death_no_smoke, x='age',hue='sex', palette='deep')
        st.pyplot(fig)
        st.subheader("The most death for non-smoking")
        st.markdown("-Men: happens in age of 45 then 75")
        st.markdown("-Women: happens in age of 60 then equally in 50 and 70")
        st.subheader("The most death for smoking")
        st.markdown("-Men: happens in age of 60 then equally in 70 and 72")
        st.markdown("-Women: happens one in each age of 50, 60, and 72")
    if selected_status == '1':
        fig = plt.figure(figsize=(20, 16))
        sns.countplot(data=death_smoke, x='age',hue='sex', palette='deep')
        st.pyplot(fig)
        st.subheader("The most death for non-smoking")
        st.markdown("-Men: happens in age of 45 then 75")
        st.markdown("-Women: happens in age of 60 then equally in 50 and 70")
        st.subheader("The most death for smoking")
        st.markdown("-Men: happens in age of 60 then equally in 70 and 72")
        st.markdown("-Women: happens one in each age of 50, 60, and 72")

if chart_visual == 'Count Plots':
       st.subheader("Plot4: Shows Count of death based on follow-up Time Under 100 Days")
       fig = plt.figure(figsize=(20, 16))
       sns.countplot(x='time', data=time100, palette='deep')
       st.pyplot(fig)

if chart_visual == 'Count Plots':
    st.subheader("Plot5: Shows Count of death based on follow-up Time Above 100 Days")
    fig = plt.figure(figsize=(20, 16))
    sns.countplot(x='time', data=time250, palette='deep')
    st.pyplot(fig)

elif chart_visual == 'Scatterplots':
     st.sidebar.subheader("Scatterplots Settings")
     st.subheader("Scatterplots: Shows the relationships between every two selected numerical features")
     try:
        x_values = st.sidebar.selectbox('X axis', options=selected_columns)
        y_values = st.sidebar.selectbox('Y axis', options=selected_columns)
        plot = px.scatter(data_frame=heart, x=x_values, y=y_values)
        # dsplay the chart
        st.plotly_chart(plot)
     except Exception as e:
        print(e)

elif chart_visual == 'Heatmaps':
     try:
         st.subheader("Features Correlation with DEATH_EVENT for all patients")
         plot = px.density_heatmap(heart.corr()[['DEATH_EVENT']].sort_values(by='DEATH_EVENT', ascending=False))
         # dsplay the chart
         st.plotly_chart(plot)
         st.subheader("The Most 5 Correlated features for all patients:")
         st.markdown("- time")
         st.markdown("- serum_creatinine")
         st.markdown("- ejection_fraction")
         st.markdown("- age")
         st.markdown("- serum_sodiumn")

         st.subheader("Features Correlation with DEATH_EVENT for Women")
         plot = px.density_heatmap(women.corr()[['DEATH_EVENT']].sort_values(by='DEATH_EVENT', ascending=False))
        # dsplay the chart
         st.plotly_chart(plot)
         st.subheader("The Most 5 Correlated features for Women:")
         st.markdown("- time")
         st.markdown("- serum_creatinine")
         st.markdown("- serum_sodiumn")
         st.markdown("- smoking")
         st.markdown("- ejection_fraction")
         st.subheader("smoking has higher positive correlation with death among women than men:")
         st.markdown("-75% of smoked women died")
         st.markdown("-27.6% of smoked men died")


         st.subheader("Features Correlation with DEATH_EVENT for Men")
         plot = px.density_heatmap(men.corr()[['DEATH_EVENT']].sort_values(by='DEATH_EVENT', ascending=False))
         st.plotly_chart(plot)
         st.subheader("The Most 5 Correlated features for Men:")
         st.markdown("- time")
         st.markdown("- ejection_fraction")
         st.markdown("- serum_creatinine")
         st.markdown("- serum_sodium")
         st.markdown("- creatinine_phosphokinase")
     except Exception as e:
        print(e)

elif chart_visual == 'Histograms':
     st.sidebar.subheader("Important Features from Regression and Classification Modeling")
     st.sidebar.markdown("See Number of Death based on important features level")
     features = ('time', 'ejection_fraction', 'serum_sodium', 'serum_creatinine',
                                              'creatinine_phosphokinase', 'platelets')
     st.subheader("Number of Death based on Important Features level and Gender")
     try:
        x_values = st.sidebar.selectbox('Select Feature', options=features)
        selected_status = st.sidebar.selectbox('Select Sex/Gender',
                                               options=['0', '1'])
        st.sidebar.subheader("Normal range for features:")
        st.sidebar.markdown("ejection fraction: 50%~75%")
        st.sidebar.markdown("serum sodium: 135~145(mEq/L)")
        st.sidebar.markdown("serum creatinine for women: 0.6~1.1 mg/dL")
        st.sidebar.markdown("serum creatinine for men: 0.7~1.3 mg/dL")
        st.sidebar.markdown("creatinine phosphokinase: 10~120(mcg/L)")
        st.sidebar.markdown("platelets:150000~450000 per microliter")
        if selected_status == "0":
            plot = px.histogram(death_w, x=x_values)
            st.plotly_chart(plot)
            st.subheader("Time is the most negative correlated feature with death")
            st.markdown("- 51% of death happened before 50 follow-up days for all patients")
            st.subheader("Percentage of patients who died with the abnormality level of important features:")
            st.markdown("Ejection_fraction: 85.4% (most important feature after time)")
            st.markdown("Creatinine_phosphokinae: 80%")
            st.markdown("Serum_creatinine: 70.6% for women and 30.65% for men")
            st.markdown("Serum_sodium: 43.75%")
            st.markdown("Platelets: 16.67%")

        if selected_status == "1":
            plot = px.histogram(death_m, x=x_values)
            st.plotly_chart(plot)
            st.subheader("Time is the most negative correlated feature with death")
            st.markdown("- 51% of death happened before 50 follow-up days for all patients")
            st.subheader("Percentage of patients who died with the abnormality level of important features:")
            st.markdown("Ejection_fraction: 85.4% (most important feature after time)")
            st.markdown("Creatinine_phosphokinase: 80%")
            st.markdown("Serum_creatinine: 70.6% for women and 30.65% for men")
            st.markdown("Serum_sodium: 43.75%")
     except Exception as e:
        print(e)
