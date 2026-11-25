# PART A 
initial_balance = 10000
monthly_deposit = 2000
months = 24
annual_rate = 0.06

balance = initial_balance
balances = []

for month in range(1, months + 1):# 月利率計息，加當月固定存款，更新目前餘額
    # 先計息，再加入當月存款，更新 balance
    balance = balance * (1 + annual_rate / 12) + monthly_deposit
    # 將新的 balance 加入 balances
    balances.append(balance)     # 將該月底餘額存入串列
# 使用 balances 的索引輸出指定月份
print(f"第 1 個月底餘額：{balances[0]:.2f}") #索引從0開始
print(f"第 12 個月底餘額：{balances[11]:.2f}")
print(f"第 24 個月底餘額：{balances[23]:.2f}")


# PART B
rates = [0, 0.03, 0.06]
final_balances = []
for rate in rates:
    balance = initial_balance  # 每換一個利率，重新設定初始餘額
    for month in range(months):  # 在 PART A 已經設定 MONTH = 24
        # 更新 24 個月的 balance
        balance = balance * (1 + rate / 12) + monthly_deposit
    # 使用 append() 將期末餘額加入 final_balances
    final_balances.append(balance) # 必須等內層 24 個月全部計算完畢（縮排在內層迴圈外），才將第 24 個月的期末餘額存入

# 使用索引，輸出各利率與對應的期末餘額
for i in range(len(rates)):
    print(f"年利率 {rates[i] * 100:.0f}% 的期末餘額為：{final_balances[i]:.2f}")


# PART C
student_id = input("請輸入學號：")
d = int(student_id[-1])
target = 61000 + 250 * d
best_rate = 0
best_balance = 0
min_error = float("inf")
for i in range(1201):
    rate = i / 10000 # 例如 0.0001 代表年利率 0.01%
    balance = initial_balance
    for month in range(months):
# 用目前 rate 試算 24 個月後的 balance
        balance = balance * (1 + rate / 12) + monthly_deposit
    error = abs(balance - target) #絕對值 消除正負方向差異以單純比較接近程度
    if error < min_error:
# 更新最小誤差、最佳年利率和對應餘額
        min_error = error
        best_rate = rate
        best_balance = balance
# 輸出搜尋結果
print(f"目標金額：{target:.2f}")
print(f"搜尋的候選利率數量：{1201}")
print(f"最佳年利率為：{best_rate * 100:.2f}%")
print(f"對應的期末餘額：{best_balance:.2f}")
print(f"與目標的絕對差距：{min_error:.2f}")


#PART D

count = 0
for i in range(len(rates)):
    rate = rates[i]
    balance = final_balances[i]
    if balance >= target:
        # 輸出 rate 及「達成」
        print(f"年利率 {rate * 100:.0f}% :達成")
        # 將 count 加 1
        count += 1
    else:
# 輸出 rate 及「未達成」
        print(f"年利率 {rate * 100:.0f}% :未達成")
# 輸出達成目標的利率數量
print(f"達成目標的利率數量：{count}")

# ===== AI 使用與學習說明 =====
# 1. 使用工具: Gemini 用於分段邏輯拆解，釐清迴圈觀念
# 2. 協助內容: 搞懂append放在內外層迴圈的差異, 了解很多python專有語法，還有怎麼用索引同步兩個串列的資料
# 3. 驗證或修改經驗: 原本在part c 誤把內層迴圈寫在外層(利率)迴圈外面，後來經AI 修正，0% 的利率結果頷首算的一樣，其他利率也都正確


