import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.markdown("""
    <style>
    body {
        background-image: url("https://raw.githubusercontent.com/niharpalem/eda/806b90f2875a0d5d4afc9001f8affedd14669c15/how-artificial-intelligence-is-shaping-data-analytics.jpg");
        background-size: cover;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title('Advanced EDA App')
    st.markdown("Upload a CSV file and this app will perform advanced exploratory data analysis (EDA) on it.")

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

        if st.checkbox('Show data types'):
            st.table(data.dtypes)

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

        st.markdown("### Advanced Analysis")
        if st.checkbox('Show correlation heatmap'):
            corr = data.corr()
            fig, ax = plt.subplots(figsize=(5,5))
            sns.heatmap(corr, annot=True, ax=ax)
            st.pyplot(fig)

        if st.checkbox('Show pairplot'):
            fig = sns.pairplot(data)
            st.pyplot(fig)

        st.markdown("### Custom Plot")
        if st.checkbox('Create a custom plot'):
            plot_types = ['scatter', 'line', 'area', 'bar', 'box', 'histogram']
            plot_type = st.selectbox('Select plot type', plot_types)
            x_var = st.selectbox('Select x variable', data.columns)
            y_var = st.selectbox('Select y variable', data.columns)
            color = st.color_picker('Pick a color for your plot')
            fig = px.__dict__[plot_type](data, x=x_var, y=y_var, color_discrete_sequence=[color])
            st.plotly_chart(fig)

    st.markdown("---")
    st.markdown("#### Connect with me:")
    st.markdown("[GitHub](https://github.com/niharpalem) | [Medium](https://medium.com/@nihar-palem)")

if __name__ == "__main__":
    main()
