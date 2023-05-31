import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Define a function to generate a statistical summary
def generate_summary(df):
    summary = df.describe()
    return summary

# Define the Streamlit app
def app():
    st.title('Excel File Analyzer')

    # Allow the user to upload an Excel file
    file = st.file_uploader('Upload Excel file', type=['xlsx', 'xls'])

    if file is not None:
        # Read in the Excel file as a Pandas DataFrame
        df = pd.read_excel(file)

        # Generate a statistical summary
        summary = generate_summary(df)

        # Display the summary in a table
        st.subheader('Statistical Summary')
        st.dataframe(summary)

        # Display visualizations
        st.subheader('Data Visualization')

        # Plot a histogram for each numerical column
        numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
        for column in numerical_columns:
            fig, ax = plt.subplots()
            sns.histplot(data=df, x=column, ax=ax)
            st.pyplot(fig)

        # Plot a box plot for each numerical column
        for column in numerical_columns:
            fig, ax = plt.subplots()
            sns.boxplot(data=df, y=column, ax=ax)
            st.pyplot(fig)

        # Plot a correlation heatmap
        corr_matrix = df.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
        st.subheader('Correlation Heatmap')
        st.pyplot(fig)

        # Plot a heatmap for the correlation between each column with others
        st.subheader('Correlation Heatmap Between Columns')
        fig, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

        # Plot a bar chart for each categorical column
        categorical_columns = df.select_dtypes(include=['object']).columns
        for column in categorical_columns:
            value_counts = df[column].value_counts()
            fig, ax = plt.subplots()
            sns.barplot(x=value_counts.index, y=value_counts.values, ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
            st.subheader(f'Bar Chart for {column}')
            st.pyplot(fig)

# Run the app
if __name__ == '__main__':
    app()
