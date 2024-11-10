from ast import Return
from statsmodels.tsa.arima.model import ARIMA

# Use only BlackRock data for time series forecasting
model = ARIMA(returns['BLK'], order=(5, 1, 0))  # ARIMA(5, 1, 0) model
model_fit = model.fit()

# Summary of the model
print(model_fit.summary())

# Make predictions for the next 30 days
forecast = model_fit.forecast(steps=30)
print(forecast)