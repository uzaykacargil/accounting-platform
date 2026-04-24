# This file stores constants and definitions for our financial indicators.
# Keeping them here makes it easier to change names or add descriptions later.

# Profitability Metrics
GROSS_MARGIN = "Gross Margin (%)"
OPERATING_MARGIN = "Operating Margin (%)"
NET_MARGIN = "Net Margin (%)"

# Liquidity Metrics
CURRENT_RATIO = "Current Ratio"
QUICK_RATIO = "Quick Ratio"

# Cash Flow Metrics
FREE_CASH_FLOW = "Free Cash Flow"
OPERATING_CASH_FLOW_RATIO = "Operating Cash Flow Ratio"

# Descriptions to help beginners understand the metrics
INDICATOR_DESCRIPTIONS = {
    GROSS_MARGIN: "The percentage of revenue left after deducting the cost of goods sold.",
    OPERATING_MARGIN: "The percentage of revenue left after paying for operating expenses.",
    NET_MARGIN: "The percentage of revenue that remains as profit after all expenses and taxes.",
    CURRENT_RATIO: "Measures a company's ability to pay short-term obligations (Current Assets / Current Liabilities). Higher is generally better.",
    QUICK_RATIO: "Similar to Current Ratio but excludes inventory (which is harder to sell quickly).",
    FREE_CASH_FLOW: "The cash a company generates after accounting for cash outflows to support operations and maintain its capital assets.",
    OPERATING_CASH_FLOW_RATIO: "Measures how well current liabilities are covered by the cash flow generated from operations."
}
