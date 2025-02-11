import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title
st.title("Real-Time Competitor Analysis for E-commerce")

# Create a sidebar for user input
st.sidebar.header("Select Competitors")
competitors = st.sidebar.multiselect("Select competitors to analyze", ["Amazon", "eBay", "Walmart", "Best Buy"])

# Load data (replace with your own data loading logic)
@st.cache
def load_data():
    # Replace with your own data loading logic
    data = pd.DataFrame({
        "Competitor": ["Amazon", "eBay", "Walmart", "Best Buy"],
        "Price": [100, 120, 90, 110],
        "Rating": [4.5, 4.2, 4.1, 4.3]
    })
    return data

# Load data
data = load_data()

# Filter data based on user selection
filtered_data = data[data["Competitor"].isin(competitors)]

# Create a line chart to display price comparison
st.header("Price Comparison")
fig, ax = plt.subplots()
sns.lineplot(x="Competitor", y="Price", data=filtered_data)
st.pyplot(fig)

# Create a bar chart to display rating comparison
st.header("Rating Comparison")
fig, ax = plt.subplots()
sns.barplot(x="Competitor", y="Rating", data=filtered_data)
st.pyplot(fig)

# Create a table to display detailed comparison
st.header("Detailed Comparison")
st.write(filtered_data)
