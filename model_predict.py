import argparse
import joblib
from sklearn.metrics import classification_report
import pandas as pd
from datetime import datetime


def predict_transaction(model_path, file_path):
    """
    Function to predict transaction status

	Parameters
	----------
	model_path : str
	    Path of the ML trained model saved.
	file_path : str
	    Path of the test set stored in any csv file.

	Returns
	-------
	file_name : str
	    Location of the result file stored
    """

    try:
        data = pd.read_csv(file_path)
        model = joblib.load(model_path)
        # drop the columns that are not important similar to the way it is removed while building the model
        data_df = data.drop(columns=['receipt_id', 'company_id', 'matched_transaction_id', 'feature_transaction_id',
                                     'DifferentPredictedDate', 'DifferentPredictedTime'])
        y_pred = model.predict(data_df)
        data['Transaction_Status'] = y_pred
        now = datetime.now()
        current_time = now.strftime("%d-%m-%Y_%H-%M-%S")
        file_name = "results/receipt_matching_result_" + str(current_time)
        data.to_csv(file_name, index=False)

        return file_name
    except Exception as e:
        return ("Error in running for failed jobs : " + str(e))


if __name__ == '__main__':
    predict_future_transactions = predict_transaction(model_path="saved_model/tide_finalized_model_1.sav",
                                                      file_path="data/test.csv")
    print("Results are stored in following location :: {}".format(predict_future_transactions))
