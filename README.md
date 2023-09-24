# Quantitative_Trading_LSTM
## Introduction
(This project is collaborated by two sophomore students, not yet completed)<br><br>
With the aim to gain a deeper understanding and direction to know more about quant trading, we would like to build a project including price prediction, backtesting and algo-trading to identify the major obstacles in it.
<p >Therefore, instead of achieving highly efficient methods, we tend to perform a joruney of how we discover the unknown in quant trading.

<p> The project will mainly be dividied into two parts: price prediction with LSTM model and algo-trading.</p>

## Structure of the project
### Model & Research
In this directory, we will show the process how we train the best-fit LSTM model for each target stock. And the result will be stored to Resources directory

### Resources
The best-models trained for every target stock will be placed here. A function is designed to gain the latest sets of predicted closing price of a stock by accessing its best-models here.

We want to train the model to fit to the test data.

## Process 

### 1. Stock Filtering
<p>There are two perspective:</p>

<p>1.1 Financial Reasoning<br>
Because price fluctuations caused by <ins><b>public opinion</b></ins> or <b><ins>breaking news</ins></b> cannot be predicted by machine learning with historical data, I would like to select stocks with <b><ins>low public concern or high institutional investor ownership</ins></b>. Meanwhile, we are looking for stocks with <b><ins>high volatility</ins></b> to ensure a certain amount of shortfall.<br></p>
       
<p>Therefore, our target stock should fulfil the following conditions:
<ol>
       <li>relatively low to medium market Capital</li>
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


## Method of Price Prediction
<p>

### A Few Reasones to Use LSTM:
LSTM is a improved variant of RNN, specialised in learning data in sequence, such as time series data. Its combination of forget gate, input gate and output gate could catch the long-term pattern effectively.
<p> Also, please note that time series data can be divided into 4 parts: <b>Trend, Cycle, Seasonality, Noise</b> 

### Application of LSTM model:
<p>I highly recommend going to the research file of any stock to know more about how we train a model and get the predicted price. It will be more clean and easier to explain with code.</p>


