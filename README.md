# Tide-Receipt Matching Data Science Challenge

## Dataset

Dataset used in this project can be found [here](https://github.com/sandeepKondaveeti/Tide_Receipt_Matching-/blob/main/data/data_interview_test.csv).

## Approach

1. Importing the libraries and data.
2. Data Preprocessing
	- Understanding type of features in the data (Ex: Categorical/Continuous)
	- Creating the Labelled column from the data (Arriving at Transaction_Status which is target variable achieved using matched_transaction_id and 	             feature_transaction_id)
	- Drop the irrelevant features (matched_transaction_id and feature_transaction_id)
3. Exploratory Data Analysis (EDA)
	- Visualize the target feature to understand the class imbalance.
	- Correlation Matrix to understand correlations of one feature with others in the dataset.
	- Drop the less important features (Based on correlation matrix score of features with the target variable, DifferentPredictedDate and                               DifferentPredictedTime were having the least score.)
4. Balancing the DataSet using SMOTE
	- Transform the dataset to respond to class imbalance. (Instead of using sampling techniques like oversampling and undersampling which helps in balancing           out data but does not add any new information to the model, hence used SMOTE which is a type of data augmentation for minority class)
5. Train and Test split Dataset.
6. Hypermater tuning with multiple Models.
	- Created a utility function using GridSearchCV with a CV score of 10 to run ML models with different combinations of hyper parameters. (Since the dataset           is small used GridSearchCV to run on all the combinations of hyperparameters passed to the models, else if the dataset is huge we can consider using               RandomisedSearchCV)
	- Run different models and analysed the classification report to understand precision/recall/f1-score. (Since it is an imbalance dataset we can avoid using accuracy as performance evaluation metric for model and use precision/recall/f1Score)
7. Save the model with better evaluations in terms of precision/recall/f1Score.

## Code

The code used in this project is inside **Final_Submission.ipynb**.

## Run Notebook instance

- To run this project you will need some software, like Anaconda, which provides support for running .ipynb files (Jupyter Notebook).


## Run model_predict.py

- Store the data to predict as 'test.csv' file in 'data/' folder.
- Install dependencies from requirements.txt
- Run file as python3 model_predict.py 
- Results will be stored for the test dataset provided in 'results/' folder


## Conclusion

After analysing the features provided, dropped some of the features which are not important. Drawn relevant insights from our **Exploratory Data Analysis (EDA)** and modelled the data over various classification algorithms with combination of hypermareters and clearly see that **Random Forest Classifer** provides best results.
