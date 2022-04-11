import numpy as np
from sklearn import metrics
from sklearn.metrics import r2_score

def getRegressorInfo(regressor, x_test, y_test, y_pred):
    print("Info related to ML model:")
    print('\tIntercept: ', regressor.intercept_)
    print('\tCoefficient: ', regressor.coef_)
    print('\tMean Absolute Error for test data: ', metrics.mean_absolute_error(y_test, y_pred))
    print('\tMean Squared Error for test data: ', metrics.mean_squared_error(y_test, y_pred))
    print('\tRoot Mean Squared Error for test data: ', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    print('\tR2 score for test data: ', r2_score(y_test, y_pred))
    print("\n")