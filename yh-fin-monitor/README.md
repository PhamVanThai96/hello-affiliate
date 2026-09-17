This project is designed to monitor financial data using the Yahoo Finance API. It provides tools for analyzing stock market trends and generating reports based on the specified configurations.

## Activate a virtual environment (optional but recommended):

    python3 -m venv path/to/venv
    source path/to/venv/bin/activate

## To install the required packages, run the following command in your terminal:
    
    pip install -r dev/requirements.txt

## Folder Structure:

/dev: Contains development-related files, including requirements.txt and configuration files for analysis.
/output: Directory where analysis results and reports will be saved.
/skills: Contains scripts and modules for performing various financial analyses.
/documents: Documentation and additional resources related to the project.
/ai-session: Stores session data for the AI agent used in the analysis.

## Configuration:
The configuration for the analysis is specified in the `dev/config_analysis.json` file. You can modify the following parameters:
- `tickers`: A list of stock tickers to analyze (e.g., ["STB.VN", "VNM.VN"]).
- `period`: The time period for the analysis (e.g., "12mo" for 12 months).
- `interval`: The data interval (e.g., "1d" for daily data).
- `candle_order`: The order of the candlestick chart to be generated.
- `lookback`: The number of past data points to consider for analysis.
- `output_dir`: The directory where output files will be saved.

After modifying the configuration file and activate the virtual environment, you can run the analysis script to generate reports based on the specified parameters.

    python3 dev/analysis_script.py

## Please update ai-sesion at the end of the analysis to save the session data for future reference.