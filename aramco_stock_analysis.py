import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt

# Create Ticker object for Aramco
aramco = yf.Ticker("2222.SR")

# Get historical data
aramco_history = aramco.history(period="max")

# Display first few rows
print(aramco_history.head())

info = aramco.info

sector = info.get('sector', 'Not Available')
country = info.get('country', 'Not Available')

print(f"Sector: {sector}")
print(f"Country: {country}")

df = pd.DataFrame(aramco_history)
print("\nFirst 5 rows of stock data:")
print(df.head())

# 4. Plot closing price
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['Close'], color='darkgreen', label='Closing Price')
plt.title(f"Saudi Aramco (2222.SR) - Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Close Price (SAR)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Plot trading volume
plt.figure(figsize=(14, 4))
plt.plot(df.index, df['Volume'], color='steelblue', label='Volume Traded')
plt.title("Trading Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

df = aramco.history(period="1d")  # Today's or latest data

# Extract latest values
latest = df.iloc[-1]
labels = ['Open', 'High', 'Low', 'Close']
values = [latest['Open'], latest['High'], latest['Low'], latest['Close']]

# Pie chart
plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Aramco Stock Price Components (Latest Day)")
plt.axis('equal')
plt.show()
