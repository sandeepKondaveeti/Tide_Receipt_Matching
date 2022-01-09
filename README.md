# Tide-Receipt Matching Data Science Challenge

## Results

## Dataset

Dataset used in this project can be found [here](https://github.com/sandeepKondaveeti/huggleCare/blob/main/corona_tested_individuals_ver_006.english.csv).

## Approach
1. Importing the libraries and data.
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Balancing the DataSet using SMOTE
5. Train and Test split Dataset.
6. Hypermater tuning with multiple Models.
8. Conclude model with better results.

## Code

The code used in this project is inside **Final_Submission.ipynb**.

## Run Notebook instance

- To run this project you will need some software, like Anaconda, which provides support for running .ipynb files (Jupyter Notebook).


## Run model_predict.py

- Store the data to predict as `test.csv` file in `data/` folder.
- Install dependencies from requirements.txt
- Run file as python3 model_predict.py 

## Conclusion

After analysing the features provided, dropped some of the features which are not important. Drawn relevant insights from our **Exploratory Data Analysis (EDA)** and modelled the data over various classification algorithms with combination of hypermareters and clearly see that **Random Forest Classifer** provides best results.

