import sys
import os
import streamlit as st
import plotly.express as px

# --- Setup to find our other files ---
# This tells Python to look in the main folder for our other files.
# It's a bit advanced, but necessary for the project structure.
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# --- Import our custom code ---
from data_ingestion.data_ingestion_and_normalization import load_financial_data
from financial_analysis.cash_flow_calculator import run_all_cash_flow_calculations
from financial_analysis.profitability_calculator import run_all_profitability_calculations
from financial_analysis.liquidity_calculator import run_all_liquidity_calculations
from core.financial_indicators import INDICATOR_DESCRIPTIONS

# --- Set up the Web Page ---
st.set_page_config(
    page_title="Financial Health Dashboard",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Financial Health Dashboard")
st.write("Welcome to the beginner-friendly financial monitoring platform! We are using fake data to learn how to analyze company health.")

# --- Load and Prepare Data ---
# We use st.cache_data so we don't reload the data every time we click a button
@st.cache_data
def get_raw_data():
    return load_financial_data()

def calculate_metrics(df):
    # We make a copy so we don't accidentally modify the raw data in Streamlit's state
    df_calc = df.copy()
    df_calc = run_all_cash_flow_calculations(df_calc)
    df_calc = run_all_profitability_calculations(df_calc)
    df_calc = run_all_liquidity_calculations(df_calc)
    
    # Calculate custom metrics for user request
    df_calc['Equity-ratio'] = df_calc['Total Equity'] / df_calc['Total Assets']
    df_calc['EBIT-Margin'] = df_calc['EBIT'] / df_calc['Revenue']
    return df_calc

raw_data = get_raw_data()

# --- Dashboard Layout ---
# We use tabs to organize our different types of analysis
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Profitability", "Liquidity", "Cash Flow", "Custom Metrics"])

with tab1:
    st.header("Data Overview")
    st.write("You can **edit** the raw data below! All charts and metrics will update automatically.")
    edited_raw_data = st.data_editor(raw_data, num_rows="dynamic", use_container_width=True)

# Now calculate the final metrics using the edited data
data = calculate_metrics(edited_raw_data)

with tab2:
    st.header("Profitability Analysis")
    st.write("How good are these companies at making a profit?")
    
    # We let the user choose which metric to see
    metric_choice = st.selectbox(
        "Choose a metric to view:",
        ["Gross Margin (%)", "Operating Margin (%)", "Net Margin (%)"]
    )
    
    # Show the explanation from our core file
    st.info(INDICATOR_DESCRIPTIONS[metric_choice])
    
    # Create a simple bar chart
    fig = px.bar(data, x='Company', y=metric_choice, color='Company', title=f"{metric_choice} by Company")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Liquidity Analysis")
    st.write("Can these companies pay their short-term bills?")
    
    metric_choice = st.selectbox(
        "Choose a metric to view:",
        ["Current Ratio", "Quick Ratio"]
    )
    
    st.info(INDICATOR_DESCRIPTIONS[metric_choice])
    
    fig = px.bar(data, x='Company', y=metric_choice, color='Company', title=f"{metric_choice} by Company")
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.header("Cash Flow Analysis")
    st.write("How much actual cash do these companies have flowing in?")
    
    metric_choice = st.selectbox(
        "Choose a metric to view:",
        ["Free Cash Flow", "Operating Cash Flow Ratio"]
    )
    
    st.info(INDICATOR_DESCRIPTIONS[metric_choice])
    
    fig = px.bar(data, x='Company', y=metric_choice, color='Company', title=f"{metric_choice} by Company")
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.header("Custom Metrics")
    st.write("Table showing Equity-ratio, EBIT, and EBIT-Margin for all companies.")
    
    # Select only the requested columns
    custom_df = data[['Company', 'Equity-ratio', 'EBIT', 'EBIT-Margin']]
    
    # Format the columns for better display
    st.dataframe(
        custom_df.style.format({
            'Equity-ratio': '{:.2%}',
            'EBIT': '${:,.2f}',
            'EBIT-Margin': '{:.2%}'
        }),
        use_container_width=True
    )

# Add a little footer
st.markdown("---")
st.write("Built with Streamlit & Python!")
