import streamlit as st
import pandas as pd
import plotly.express as px

st.title("?? Interactive HR Dashboard")

# CSV load ????????
data = pd.read_csv("hr_data.csv")

# Sidebar filter
department = st.sidebar.multiselect(
    "Select Department",
    options=data["Department"].unique(),
    default=data["Department"].unique()
)
filtered_data = data[data["Department"].isin(department)]

# Show filtered data
st.subheader("Employee Data")
st.dataframe(filtered_data)

# Salary distribution
st.subheader("Salary Distribution")
fig = px.histogram(filtered_data, x="Salary", nbins=20, title="Salary Distribution")
st.plotly_chart(fig)

# Attrition pie chart
st.subheader("Attrition Count")
fig2 = px.pie(filtered_data, names="Attrition", title="Attrition Count")
st.plotly_chart(fig2)

# Average Salary by Department
st.subheader("Average Salary by Department")
avg_salary = filtered_data.groupby("Department")["Salary"].mean().reset_index()
fig3 = px.bar(avg_salary, x="Department", y="Salary", title="Average Salary by Department")
st.plotly_chart(fig3)
