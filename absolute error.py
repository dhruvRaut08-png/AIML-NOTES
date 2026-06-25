import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error

y_true = np.array([3.0, -0.5, 2.0, 7.0 ,5.0])
y_pred = np.array([2.5, 0.0, 2.0, 8.0 ,4.2])

mae_sklearn = mean_absolute_error(y_true, y_pred)
mse_sklearn = mean_squared_error(y_true, y_pred)
rmse_sklearn = np.sqrt(mse_sklearn)

print("--- scikit-LearnResults ---")
print(f"Mean Absolute Error (MAE): {mae_sklearn:.4f}")
print(f"Mean Absolute Error (MSE): {mse_sklearn:.4f}")
print(f"Root Mean Squared Error: {rmse_sklearn:.4f}")