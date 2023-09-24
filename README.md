# Quantitative_Trading_LSTM
## Introduction
(This project is collaborated by two sophomore students, not yet completed)<br><br>
With the aim to gain a deeper understanding and direction to know more about quant trading, we would like to build a project including price prediction, backtesting and algo-trading to identify the major obstacles in it.
<p >Therefore, instead of achieving highly efficient methods, we tend to perform a joruney of how we discover the unknown in quant trading.

<p> The project will mainly be dividied into two parts: price prediction with LSTM model and algo-trading.</p>

## Process 

### 1. Stock Filtering
<p>There are two perspective:</p>

<p>1.1 Financial Reasoning<br>
Because price fluctuations caused by <ins><b>public opinion</b></ins> or <b><ins>breaking news</ins></b> cannot be predicted by machine learning with historical data, I would like to select stocks with low public concern or high institutional investor ownership. Meanwhile, we are looking for stocks with high volatility to ensure a certain amount of shortfall.<br></p>
       
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

### 3. Pick the most accurate model by regenerating with the set of the optimised hyperparameter

### 4. Trade with different strategy


<P> 
## Method of Price Prediction
<p>LSTM will be used widely in this project for predicting stock closing price although we desire to try other ways later<br>

### A Few Reasones to Use LSTM:
LSTM is a improved variant of RNN, specialised in learning data in sequence, such as time series data. Its combination of forget gate, input gate and output gate could catch the long-term pattern effectively.
<p> Also, please note that time series data can be divided into 4 parts: <b>Trend, Cycle, Seasonality, Noise</b> 




### Application of LSTM model:
<p>At this stage, we will only use the historical closing price as the input during the training proess.<br>
And, we will only split selected historical data into training and test dataset, in which the test dataset will be the one closer to the present</p>
<img src="README_source/pic1.jpg" alt="替代文本" style="width: 1500%; height: auto;">

To make sure that LSTM model do learn a productive pattenrn in the training process and there is enough training and testing data, we only select stocks with a        final monotone trend of closing price of more than 8 years as target.<br> 
Also, we train the model only using the monotone trend for every target stock.


  
<img src="README_source/pic2.jpg" alt="替代文本" style="width: 1500%; height: auto;">





## Structure of the project
### Model & Research
In this directory, we will show the process how we train the best-fit LSTM model for each target stock. And the result will be stored to Resources directory

### Resources
The best-models trained for every target stock will be placed here. A function is designed to gain the latest sets of predicted closing price of a stock by accessing its best-models here.

We want to train the model to fit to the test data.
