# Gradient_Descent
Applying Gradient Descent on Data mapping "TV_commercials" to "Increase in Sales%". 

Implementation of the Gradient Descent Optimizer with Early Stopping and dynamic Learning Rate for Liner Regression problem.


# Dependencies

Pandas

# Dataset

The dataset has 2 columns, TV commercials and % increase of sales. I have used % increase of sales as the output(Y) with TV commercials as input(X). Thus aiming to find a linear function f(X) = Y.

# Script 1: data_parser.py

This script is used as a helper script, to read in the csv file. Once it is read in, the missing values are replaced with a 0. The desired columns alone are chosen and are returned as a python array. For the purpose of demo, only the first 1000 rows are returned.

# Script 2: gradient_descent.py

The actual action happens here.

I have implemented a vanilla gradient descent method in step_gradient function. You can see the script for in-depth comments for each line of code.

I have also added 2 different modifications to the vanilla gradient descent optimizer. I have added an early stopping feature, which can be controlled by early_stop_number parameter and also I have added adaptive learning rate, through which the learning rate increases by .00002 everytime the error value decreases consecutively for more than 3 times. This aims to increase the computational speed. This feature can be controlled via the modify_lr flag.

