import pandas as pd

def calculate_gross_margin(df):
    """
    Calculates Gross Margin.
    Formula: Gross Profit / Revenue
    """
    result_df = df.copy()
    result_df['Gross Margin (%)'] = (result_df['Gross Profit'] / result_df['Revenue']) * 100
    return result_df

def calculate_operating_margin(df):
    """
    Calculates Operating Margin.
    Formula: Operating Profit / Revenue
    """
    result_df = df.copy()
    result_df['Operating Margin (%)'] = (result_df['Operating Profit'] / result_df['Revenue']) * 100
    return result_df

def calculate_net_margin(df):
    """
    Calculates Net Margin.
    Formula: Net Income / Revenue
    """
    result_df = df.copy()
    result_df['Net Margin (%)'] = (result_df['Net Income'] / result_df['Revenue']) * 100
    return result_df

def run_all_profitability_calculations(df):
    """
    Helper to run all profitability metrics at once.
    """
    df = calculate_gross_margin(df)
    df = calculate_operating_margin(df)
    df = calculate_net_margin(df)
    return df
