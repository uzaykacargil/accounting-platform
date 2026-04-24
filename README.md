# accounting-platform

A modular, Python-based financial monitoring platform for automated health analysis and interactive peer benchmarking.

## Overview

This project is a modular platform designed to provide comprehensive financial monitoring and analysis. It features a clear separation of concerns between data ingestion, financial calculations, and presentation, allowing for flexible deployment and analysis of financial health metrics.

## Key Features

### 1. Automated Health Analysis

- **Data Processing**: Standardizes financial data through various normalization and cleaning modules.
- **Cash Flow Monitoring**: Comprehensive analysis of cash flow cycles, inventory turnover, and working capital efficiency.
- **Profitability Analysis**: Detailed margin calculations (Gross, Operating, Net) and trend analysis.
- **Liquidity Assessment**: Tools for monitoring short-term liquidity positions.

### 2. Interactive Peer Benchmarking

- **Industry Data**: Built-in dataset of Turkish manufacturing industry financial ratios (`industry_benchmarks_tr_2022.xlsx`).
- **Health Scoring**: Automated calculation of financial health scores based on a comprehensive index.
- **Interactive Analysis**: A Streamlit-based dashboard for exploring company data and comparing it against industry benchmarks.

### 3. Modular Architecture

The platform is built with a modular design, separating different layers of the application:

- **`core/`**: Contains base utilities, financial indicators, and data structures.
- **`data_ingestion/`**: Modules for loading and processing raw financial data.
- **`financial_analysis/`**: Core logic for financial health calculations.
- **`financial_model/`**: Advanced financial modeling tools.
- **`financial_reporting/`**: Structured reporting and metrics generation.
- **`health_monitoring/`**: Health scoring and trend analysis logic.
- **`data_preprocessing/`**: Data cleaning and preparation tools.
- **`health_dashboard/`**: A Streamlit application for visualization and analysis.

## Getting Started

### Prerequisites

- Python 3.7+
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:

```bash
cd accounting-platform
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Usage

#### Running the Dashboard

The main entry point for the interactive dashboard is `health_dashboard/health_dashboard_app.py`. You can run it using Streamlit:

```bash
streamlit run health_dashboard/health_dashboard_app.py
```

#### Running Calculations

You can run specific calculation modules directly using Python. For example, to run the cash flow analysis:

```bash
python data_ingestion/data_ingestion_and_normalization.py
python financial_analysis/cash_flow_calculator.py
```

## Project Structure

```
accounting-platform/
├── core/
│   ├── utils.py
│   └── financial_indicators.py
├── data_ingestion/
│   ├── data_ingestion_and_normalization.py
│   └── ...
├── financial_analysis/
│   ├── cash_flow_calculator.py
│   └── ...
├── financial_model/
├── financial_reporting/
├── health_monitoring/
├── data_preprocessing/
├── health_dashboard/
│   └── health_dashboard_app.py
├── industry_benchmarks_tr_2022.xlsx
└── requirements.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
