def avaliar_modelo(modelo, X_test, y_test):
    from sklearn.metrics import mean_squared_error, r2_score
    import numpy as np
    y_pred = modelo.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    return mse, rmse, r2
