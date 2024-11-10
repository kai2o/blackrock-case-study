# Assuming a risk-free rate of 2% (0.02)
risk_free_rate = 0.02

# Calculate Sharpe Ratio for BlackRock
sharpe_ratio = (returns['BLK'].mean() - risk_free_rate / 252) / returns['BLK'].std()
print(f'Sharpe Ratio for BlackRock: {sharpe_ratio:.2f}')
