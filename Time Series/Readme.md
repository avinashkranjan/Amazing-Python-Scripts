# Champagne Sales Analysis

This project performs time series analysis on a dataset of monthly champagne sales. It utilizes the ARIMA and SARIMAX models for forecasting future sales trends. The analysis includes data cleaning, stationarity testing, model fitting, and visualization of results.

## Dataset

The dataset used for this analysis is "perrin-freres-monthly-champagne-.csv". It contains historical monthly sales data for champagne.


## Installation

1. Clone the repository or download the project files.
2. Install the required libraries by running the following command:


## Usage

1. Place the dataset file ("perrin-freres-monthly-champagne-.csv") in the same directory as the script.
2. Open the Python script "Time_series_product_sales_deploy.ipynb" in your preferred Python environment.
3. Run the script to perform the analysis.
4. The script will perform the following steps:
- Load and clean the dataset.
- Visualize the sales data.
- Test for stationarity using the Dickey-Fuller test.
- Perform differencing to make the data stationary.
- Fit an ARIMA model to the data and make predictions.
- Fit a seasonal ARIMA model (SARIMAX) to the data and make predictions.
- Plot the actual sales, forecasted values, and future predictions.

## Results

The script will generate visualizations of the sales data, stationarity tests, model summaries, and forecasted sales trends. The results will be displayed in the console and saved as plots in the same directory.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.


