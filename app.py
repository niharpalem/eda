
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_ace import st_ace

def main():
    st.title('CSV File Reader')

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    plots = st_ace(value="", language="python", key="ace-editor")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file, engine='python')

        if st.button('Show first 5 rows'):
            st.write(data.head())

        if st.button('Show columns and data types'):
            st.write(data.dtypes)

        if st.button('Describe the data'):
            st.write(data.describe())

        chart_type = st.selectbox('Select a chart type', ['Line', 'Bar', 'Area'])
        x_axis = st.selectbox('Select x-axis', data.columns)
        y_axis = st.selectbox('Select y-axis', data.columns)
        color = st.color_picker('Pick A Color', '#00f900')

        if st.button('Create a plot'):
            try:
                if chart_type == 'Line':
                    fig = px.line(data, x=x_axis, y=y_axis, color_discrete_sequence=[color])
                elif chart_type == 'Bar':
                    fig = px.bar(data, x=x_axis, y=y_axis, color_discrete_sequence=[color])
                elif chart_type == 'Area':
                    fig = px.area(data, x=x_axis, y=y_axis, color_discrete_sequence=[color])
                plots = st_ace(value=fig.to_json(), language="python", key="ace-editor")
            except Exception as e:
                st.write(f"An error occurred: {e}")

        if plots:
            st.plotly_chart(plots)

if __name__ == "__main__":
    main()