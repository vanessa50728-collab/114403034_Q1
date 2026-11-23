initial_balance = 10000
monthly_deposit = 2000
months = 24
annual_rate = 0.06

balance = initial_balance
balances = []

for month in range(1, months + 1):
    # 先依月利率計息，再加上當月固定存款，更新目前餘額
    balance = balance * (1 + annual_rate / 12) + monthly_deposit
    # 將該月底餘額依序存入串列中
    balances.append(balance)

# 串列索引從 0 開始，故第 1、12、24 個月分別對應索引 0、11、23
print(f"第 1 個月底餘額：{balances[0]:.2f}")
print(f"第 12 個月底餘額：{balances[11]:.2f}")
print(f"第 24 個月底餘額：{balances[23]:.2f}")
