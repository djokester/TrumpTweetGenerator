# Trump Tweet Generator
In this project we try to generate replies to tweets input by the user. The twist here is we are going to Trump style. 
This is part of my assignment for ***Language Processing for e-Learning*** course. 

## The Data 
The data provided initially was an assortment of tweets by different users. Instead of using the data provided I scraped Data off Donald Trump's Twitter handle. I chose to replace it for two reasons. 

 1. When I tried to convert the Data into matrices that could be actually used by the LSTM, I found that it was far too large to be handled by standard RAMs both on my system as well as online. The size exceeded 13 GB of space. 
 2. The second reason for replacing the tweets provided was the fact that I wouldn't be using any Language model as such, rather I would be relying largely on patterns and sequences as I would be using LSTMs. So a specific personality or trait reflected in the tweets would be much favorable in comparison to randomly chosen tweets... and we all know Donald Trump is a strong character. 

## The Model 
We used four LSTM layers of 1200, 1000, 700 and 500 hidden states and added a dropout of 0.2 after the middle two layers to prevent overfitting. We used Keras for implementing the model and trained it for 50 epochs, due to lack of computational time. Ideally the model should be trained for 200 epochs.

