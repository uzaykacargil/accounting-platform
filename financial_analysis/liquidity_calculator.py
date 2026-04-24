import pandas as pd

def calculate_current_ratio(df):
    """
    Calculates the Current Ratio.
    Formula: Current Assets / Current Liabilities
    """
    result_df = df.copy()
    result_df['Current Ratio'] = result_df['Current Assets'] / (result_df['Current Liabilities'] + 0.0001)
    return result_df

def calculate_quick_ratio(df):
    """
    Calculates the Quick Ratio.
    Formula: (Current Assets - Inventory) / Current Liabilities
    """
    result_df = df.copy()
    result_df['Quick Ratio'] = (result_df['Current Assets'] - result_df['Inventory']) / (result_df['Current Liabilities'] + 0.0001)
    return result_df

def run_all_liquidity_calculations(df):
    """
    Helper to run all liquidity metrics at once.
    """
    df = calculate_current_ratio(df)
    df = calculate_quick_ratio(df)
    return df
