# Quantitative_Trading_LSTM
(written by JoshC)
## Introduction
(This project is collaborated by two sophomore students, not yet completed)<br><br>
With the aim to gain a deeper understanding and direction to know more about quant trading, we would like to build a project including price prediction, back-testing and algo-trading to identify the major obstacles in it.
<p >Therefore, instead of achieving highly efficient methods, we tend to perform a journey of how we discover the unknown in quant trading.

<p> The project will mainly be divided into two parts: price prediction with LSTM model and algo-trading.<br></p>

## Structure of the project
### 1. Model & Research
In this directory, we will show the process how we train the best-fit LSTM model for each target stock. And the optimised model will be stored in "Resources".<br>
You may visit any directory inside "Model & Research" to see how we gain the optimised model for a target stock. 

### 2. Resources
A place to store the best-models trained for every target stock. A functionin in "predict_data.py" is designed to gain the latest set of predicted closing price of a stock by accessing trained models here.

We want to train the model to fit to the test data.

## Process 

### 1. Stock Filtering
<p>There are two perspective:</p>

<p>1.1 Financial Reasoning<br>
Because price fluctuations caused by <ins><b>public opinion</b></ins> or <b><ins>breaking news</ins></b> cannot be predicted by machine learning with historical data, I would like to select stocks with <b><ins>low public concern or high institutional investor ownership</ins></b>. Meanwhile, we are looking for stocks with <b><ins>high volatility</ins></b> to ensure a certain amount of shortfall.<br></p>
       
<p>Therefore, our target stock should fulfil the following conditions:
<ol>
       <li>relatively low to medium market capital (low level of awareness from the public)</li>
       <li>high institutional investor ownership</li>
       <li>sufficient volume or price movement </li>
</ol>
</p>


<p>1.2 Sufficient Input for training a model<br>
To ensure that LSTM model do learn a productive and solid pattenrn in the training process and there is enough training and testing data, we only select stocks with its last monotone trend of closing price of more than ~8 years as target.</p>

### 2. Select Suitable Historical Data
<p>As mentioned, we train the model by only using the last monotone trend for every target stock, like below:<br></p>

<img src="README_source/pic2.jpg" alt="替代文本" style="width: 1500%; height: auto;">

### 3. Learn the closing price of a stock by LSTM model
<p>Please note that LSTM will be used widely in this project for predicting stock closing price although we desire to try other ways later<br>
And, we will only use the historical closing price as the input during the training proess.</p>

<p>we split selected historical data into training and test dataset, in which the test dataset will be the one closer to the present</p>
<img src="README_source/pic1.jpg" alt="替代文本" style="width: 1500%; height: auto;">

<p>Then, there will be two steps.<br>
Firstly, we do train models with different combinations of hyperparameters, and pick the one that its prediction holds the least value of loss indicator (e.g. RMSE. MSE )<br>

After finding the optimised set of hyperparameters for a stock, we will train several models with it and pick the best one for predicting the future closing price during the trading session.

### 4. Trade with different strategy

There are three strategies we would like to try:
<ol>
       <li>Swing Trade<br>
       By using time lag prediction, the time lag equals to how many days of predicted closing price we could gain.<br>
       Usually, this time lag will be set to 8 days in this project because larget time lag may lead to invalid pattern for the LSTM model to learn.
       With the set of foreseeable closing price for 8 days, long/ short position could be opened and finished<br>
       </li>
       <li> Single Trade per Day<br>
              If the opening price of the day is a certain percentage lower/higher than the predicted closing price, we open a long/short position respectively at the opening of the market and end the position at the end.
       </li>
       <li>High Frequency Trade<br>
       Unfortunately, since we pay no capital on this project, it is hard for us to gain pruce trend in high frequency as historical data to train our model.<br>
       But the logic for predicting the price in high frequency could be achieved by using LSTM model with by little adjustment
       </li>
</ol>


Also, we are going to implement RSI indicator on determining the time to start a long/short position.<br>
It is because noise in time series data is unpredictable, no matter how accurate our models are. So we decide to use RSI to minimize the risk. 


## Method of Price Prediction
<p>

### A Few Reasones to Use LSTM:
LSTM is a improved variant of RNN, specialised in learning data in sequence, such as time series data. Its combination of forget gate, input gate and output gate could catch the long-term pattern effectively.
<p> Also, please note that time series data can be divided into 4 parts: <b>Trend, Cycle, Seasonality, Noise</b> 

### Application of LSTM model:
<p>I highly recommend going to the research file of any stock to know more about how we train a model and get the predicted price. It will be more clean and easier to explain with code.</p>


