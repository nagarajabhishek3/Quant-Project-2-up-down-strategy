📈 Up–Down Direction Prediction Strategy (Decision Tree)
📌 Project Overview
This project implements a machine learning–based classification strategy to predict the next-day price direction (UP/DOWN) of an equity stock using historical OHLCV data.
The strategy uses:
Daily price data from Yahoo Finance
Decision Tree Classifier
Supervised learning to classify next-day movement
The project is developed as part of a quantitative finance / algorithmic trading learning exercise.

📊 Data Source
Ticker: RELIANCE.NS
Data Provider: Yahoo Finance (via yfinance)
Frequency: Daily
Period Used: From 2010 onwards
Downloaded fields:
Open
High
Low
Close
Volume

⚙️ Feature Engineering
Target Variable
The model predicts the direction of next-day price movement:
UP → If next day Close > today Close
DOWN → If next day Close ≤ today Close
This is calculated using percentage change of next day close.

Features Used
The following variables are used as explanatory features:
Feature	Description
Open	Daily opening price
High	Daily high price
Low	Daily low price
Close	Daily closing price
Volume	Daily traded volume

🧠 Model Used
Algorithm: Decision Tree Classifier
Library: scikit-learn
Model Type: Classification
Depth: Unrestricted (max_depth=None)

The model is trained to classify whether the next trading day will be UP or DOWN.

🧪 Model Training & Evaluation
Steps followed:
Download historical data
Create next-day direction labels
Train Decision Tree model
Generate predictions on training data
Compare actual vs predicted direction
Calculate classification accuracy

Note:
This implementation evaluates in-sample accuracy and is intended for learning purposes.

📁 Project Outputs

The project generates the following files:

File	Description
RELI.xlsx	Raw downloaded price data
RELI_processed.xlsx	Processed data with target labels
RELI_prediction.xlsx	Actual vs predicted direction
model_dt_classification.pkl	Trained Decision Tree model

🛠️ Technologies Used
Python
Pandas
NumPy
yFinance
Scikit-learn
Pickle
Excel (for result inspection)

🚀 How to Run the Project
Install required libraries:
pip install yfinance pandas numpy scikit-learn

Run the script:
python updownstrategy.py

Outputs will be saved as Excel files and a serialized model.

⚠️ Disclaimer

This project is for educational and research purposes only.
It is not a trading recommendation and does not include transaction costs, slippage, or out-of-sample validation.

📌 Future Enhancements

Train/Test split or walk-forward validation
Feature engineering using indicators (RSI, EMA, ATR)
Model comparison (Random Forest, XGBoost)
Strategy backtesting with P&L
Risk-adjusted performance metrics



Abhishek N
Chartered Accountant | Quant Finance Enthusiast
Algorithmic Trading & ML Applications in Finance
