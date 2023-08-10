# Fraud Detection Script

This Python script uses machine learning algorithms to detect fraudulent transactions or activities based on historical data. It leverages the power of Random Forest classifier and handles class imbalance using SMOTE. The dataset is preprocessed with feature scaling to improve model performance.

## Requirements

To run this script, you need the following dependencies:

- Python 3
- pandas
- scikit-learn
- imbalanced-learn
- numpy

You can install the required dependencies using pip:

```bash
pip install pandas scikit-learn imbalanced-learn numpy
```

## Usage

1. Prepare your dataset: Ensure your historical data is in a CSV format with a 'Class' column containing the target variable (0 for normal, 1 for fraudulent).

2. Place your dataset: Place your data file named `data.csv` in the same directory as the `fraud_detection.py` script.

3. Run the script: Execute the script using the following command:

```bash
python fraud_detection.py
```

4. Results: The script will print the accuracy, confusion matrix, and classification report for the fraud detection model.

## Data Preprocessing

The script performs the following preprocessing steps on the dataset:

- Standard Scaling: All features are standardized to have a mean of 0 and standard deviation of 1 to improve model performance.

- Class Imbalance Handling: SMOTE (Synthetic Minority Over-sampling Technique) is used to handle class imbalance by generating synthetic samples for the minority class.

## Model

The script uses a Random Forest classifier with 100 trees for fraud detection. The model is trained on the resampled data after applying SMOTE.

Feel free to modify the script according to your dataset and experiment with different machine learning models for comparison.

