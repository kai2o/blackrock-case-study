# Example data for asset allocation
allocation = {'Stocks': 60, 'Bonds': 30, 'Real Estate': 5, 'Commodities': 5}
labels = list(allocation.keys())
sizes = list(allocation.values())

# Plot pie chart
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('BlackRock Portfolio Allocation')
plt.axis('equal')  # Equal aspect ratio ensures pie chart is circular.
plt.show()