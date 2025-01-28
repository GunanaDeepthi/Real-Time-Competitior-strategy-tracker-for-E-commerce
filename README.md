# Real-Time-Competitior-strategy-tracker-for-E-commerce
Real-Time Competitor Strategy Tracker for E-Commerce
Project Overview

This project focuses on creating a real-time competitive intelligence tool for e-commerce businesses. It provides actionable insights by monitoring competitor pricing, discount strategies, and customer sentiment. The solution leverages:

Machine Learning: Predictive modeling with ARIMA.
LLMs: Sentiment analysis using Hugging Face Transformers and Groq.
Integration: Slack notifications for real-time updates.
Features

Competitor Data Aggregation: Track pricing and discount strategies.
Sentiment Analysis: Analyze customer reviews for actionable insights.
Predictive Modeling: Forecast competitor
Slack Integration: Get real-time notifications on competitor activity.
Setup Instructions
1.Clone the repository


[ ]
git clone <repository-url>
cd <repository-directory>
2.Install Dependencies

Install the required Python libraries using pip:


[ ]
pip install .r requirements.txt
3.Configure API Keys

This project requires the following keys:

Groq API Key: For generating strategic redcommendations.
Slack Webhook URL: For sending notifications.
Steps:

Groq API Key:
sign up for a Groq account at https://groq.com.
Obtain your API Key from the Groq dashboard.
Use the API Key in the app.py file.
Slack Webhook Integration:
Go to the Slack API.
Create a new app and enable incoming webhooks.
Add a webhook to a channel and copy the generated URL.
Add this to URL to the app.py file.
4.Run the Application

Run the Streamlit app:


[ ]
streamlit run app.py
Project Files
app.py: Main application script.
scrape.py: Script for web scraping competitor data.
review.csv: Sample reviews data for sentiment analysis.
competitor_data.csv: Sample competitor data for analysis.
Usage
Launch the Steamlit app.
Select a product from the sidebar.
View competitor analysis, sentiment trends, and discount forecasts.
Get strategic recommendations and real-time Slack notifications.
License
This project is licensed by MIT License.

