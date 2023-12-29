import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title('Smart EDA App')
    st.markdown("Upload a CSV file and this app will perform basic exploratory data analysis (EDA) on it.")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file, engine='python')
        st.markdown("### Data Overview")
        if st.checkbox('Show sample data'):
            number = st.slider('Number of rows to view', min_value=1, max_value=50)
            st.dataframe(data.head(number))

        if st.checkbox('Show columns'):
            st.write(data.columns)

        if st.checkbox('Show shape'):
            st.write(data.shape)

        if st.checkbox('Show summary'):
            st.table(data.describe())

        st.markdown("### Variable Plots")
        if st.checkbox('Show plots'):
            st.markdown("#### Categorical Variables")
            select_box = st.selectbox('Choose one of the categorical variables', data.select_dtypes(include=['object']).columns)
            fig = px.histogram(data, x=select_box)
            st.plotly_chart(fig)

            st.markdown("#### Numerical Variables")
            select_box = st.selectbox('Choose one of the numerical variables', data.select_dtypes(include=['int64', 'float64']).columns)
            fig = px.histogram(data, x=select_box)
            st.plotly_chart(fig)

            st.markdown("#### Scatter Plot")
            num_vars = data.select_dtypes(include=['int64', 'float64']).columns
            var1, var2 = st.selectbox('Choose the first variable', num_vars), st.selectbox('Choose the second variable', num_vars)
            fig = px.scatter(data, x=var1, y=var2)
            st.plotly_chart(fig)

if __name__ == "__main__":
    main()
