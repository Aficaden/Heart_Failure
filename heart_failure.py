import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Mortality Prediction for Heart Failure')
st.write('The medical records collected At the Faisalabad Institute of Cardiology and at the Allied Hospital in Faisalabad (Punjab, Pakistan), during April–December 2015')
st.markdown("The dashboard will help a physicians/researcher to get to know \
more about the given datasets and it's output")
st.subheader("Project Objectives/Questions:")
st.markdown("1- What are the most important attributes are associated with mortality caused by heart failure?")
st.markdown("2- Will building a mortality prediction model based on the most important features help patients to survive?")
st.markdown("3- Does gender make differences in features importance and the mortality prediction model?")

st.sidebar.title("Select Visual Charts")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

st.subheader("Heart Failure Prediction Dataset")
heart = pd.read_csv('/Users/ac/Desktop/DATA Science/DATA6330/HW01/data/heart_failure_clinical_records_dataset.csv.xls')
st.dataframe(heart)
st.markdown("sex: 0 for women, 1 for men")
st.markdown("DEATH_EVENT: 0 for survived, 1 for death")

chart_visual = st.sidebar.selectbox('Select Charts/Plot type',
                                    options= ['Count Plots', 'Pie Charts', 'Scatterplots', 'Heatmaps', 'Histograms'])
st.sidebar.checkbox("Show Analysis by Smoking Status", True, key=1)
selected_status = st.sidebar.selectbox('Select Smoking Status',
                                       options = ['0', '1'])

death = heart[heart['DEATH_EVENT'] == 1]
death_w = death[death['sex'] == 0]
death_m = death[death['sex'] == 1]
smoke = heart[heart['smoking'] == 1]
no_smoke = heart[heart['smoking'] == 0]
death_smoke = smoke[smoke['DEATH_EVENT'] == 1]
death_no_smoke = no_smoke[no_smoke['DEATH_EVENT'] ==1]
no_smoke_w = no_smoke[no_smoke['sex'] == 0]
no_smoke_m = no_smoke[no_smoke['sex'] == 1]
smoke_w = smoke[smoke['sex'] == 0]
smoke_m = smoke[smoke['sex'] == 1]
time100 = death[death["time"] <= 100]
time250 = death[death["time"] > 100]
death_ejf= death[death['ejection_fraction'] < 50]
death_sersod= death[death['serum_sodium'] < 135]
women = heart[heart['sex'] == 0]
men =  heart[heart['sex'] == 1]



selected_columns = ('creatinine_phosphokinase', 'platelets', 'serum_creatinine',
                    'serum_sodium', 'ejection_fraction', 'anaemia', 'diabetes',
                    'high_blood_pressure', 'smoking','time', 'sex', 'DEATH_EVENT')


if chart_visual == 'Pie Charts':
    st.subheader("Pie chart1: Shows the percentage of death among male and female based on selected smoking status")
    input_col, pie_col = st.columns(2)
    if selected_status == '0':
        fig = px.pie(no_smoke, values = 'DEATH_EVENT', names = 'sex')
        fig.update_layout(width = 300,
            margin=dict(l=1,r=1,b=1,t=1))
        pie_col.write(fig)
    if selected_status == '1':
        fig = px.pie(smoke, values = 'DEATH_EVENT', names = 'sex')
        fig.update_layout(width = 300,
            margin=dict(l=1,r=1,b=1,t=1))
        pie_col.write(fig)

if chart_visual == 'Pie Charts':
    st.subheader("Pie chart2: Shows the percentage of death among patients with anaemia/no anaemia and based on selected smoking status")
    input_col, pie_col = st.columns(2)
    if selected_status == '0':
        fig = px.pie(no_smoke, values = 'DEATH_EVENT', names = 'anaemia')
        fig.update_layout(width = 300,
            margin=dict(l=1,r=1,b=1,t=1))
        pie_col.write(fig)
    if selected_status == '1':
        fig = px.pie(smoke, values = 'DEATH_EVENT', names = 'anaemia')
        fig.update_layout(width = 300,
            margin=dict(l=1,r=1,b=1,t=1))
        pie_col.write(fig)

if chart_visual == 'Pie Charts':
    st.subheader("Pie chart3: Shows the percentage of death among patients with diabetss/no diabetes and based on selected smoking status")
    input_col, pie_col = st.columns(2)
    if selected_status == '0':
        fig = px.pie(no_smoke, values = 'DEATH_EVENT', names = 'diabetes')
        fig.update_layout(width = 300,
            margin=dict(l=1,r=1,b=1,t=1))
        pie_col.write(fig)
    if selected_status == '1':
        fig = px.pie(smoke, values = 'DEATH_EVENT', names = 'diabetes')
        fig.update_layout(width = 300,
            margin=dict(l=1,r=1,b=1,t=1))
        pie_col.write(fig)

if chart_visual == 'Pie Charts':
    st.subheader(
        "Pie chart4: Shows the percentage of death among patients with high blood pressure or not and based on selected smoking status")
    input_col, pie_col = st.columns(2)
    if selected_status == '0':
        fig = px.pie(no_smoke, values='DEATH_EVENT', names='high_blood_pressure')
        fig.update_layout(width=300,
                          margin=dict(l=1, r=1, b=1, t=1))
        pie_col.write(fig)
    if selected_status == '1':
        fig = px.pie(smoke, values='DEATH_EVENT', names='high_blood_pressure')
        fig.update_layout(width=300,
                          margin=dict(l=1, r=1, b=1, t=1))
        pie_col.write(fig)

elif chart_visual == 'Count Plots':
        st.subheader("Plot1: Shows the number of men(194) and women(105)")
        fig = plt.figure(figsize=(8, 6))
        sns.countplot(x='sex', data=heart, palette='deep')
        st.pyplot(fig)

if chart_visual == 'Count Plots':
        st.subheader("Plot2: Shows the number of death based on Gender")
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
