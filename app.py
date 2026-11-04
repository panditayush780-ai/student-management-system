import http

import pandas as pd
import streamlit as st
import requests

API =  "http://127.0.0.1:8000"

st.title('Student Management System')
with st.form('add_student'):
    st.subheader('add new student')
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=0)
    grade = st.text_input('Grade')
    marks = st.number_input('Marks', min_value=0, max_value=100, step=1)
    date = st.date_input('date')
    submitted = st.form_submit_button('Add student')

    if submitted: 
        student = {
            'name': name,
            'age': age,
            'grade': grade,
            'marks': marks
        }
        response = requests.post(f'{API}/students', json=student)
        if response.status_code == 201:
            st.success('Student added successfully')
        else:
            st.error('Failed to add student . check the details and try again')

data=requests.get(f'{API}/students').json()

if data:
    df = pd.DataFrame(data)
    st.metric("Total Students", f"{len(df)}")
    st.subheader("By Grade")    
    st.bar_chart(df.groupby("grade")["marks"].sum())
    st.subheader("All Students")
    st.dataframe(df, use_container_width=True)
else:
    st.info("No students recorded yet . Add your first student using the form above.")


