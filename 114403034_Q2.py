"""資管系 Python 期中作業：商店銷售資料讀取起始程式。
請將本檔案與 mis_midterm_sales.csv 放在同一個資料夾。
教師提供的讀取區不需要修改；資料讀取後存放在 sales (list of dict)。
"""
import csv
from pathlib import Path

sales = []
file_path = Path(__file__).resolve().parent / "mis_midterm_sales.csv"

with file_path.open("r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        sales.append({
            "order_id": row["交易編號"],
            "product": row["商品名稱"],
            "category": row["類別"],
            "quantity": int(row["數量"]),
            "price": float(row["單價"]),
            "cost": float(row["單位成本"])
        })

print("成功載入", len(sales), "筆交易資料")
print("第一筆交易：", sales[0])

# ===== 以下由學生自行撰寫 =====
# Part A：總營收、總成本、總利潤、平均每筆營收
total_revenue = 0
total_cost = 0
for sale in sales:
# 取得 sale["price"]、sale["cost"] 與 sale["quantity"]
# 計算本筆營收、成本，累加到 total_revenue 與 total_cost
    print("資料比數", len(sales)) 
    print("第一筆資料", sales[0]) 
# 由總營收與總成本計算總利潤
# 計算每筆交易平均營收並輸出

# Part B：四種商品類別的營收與利潤

# Part C：商品總營收前三名

# Part D：學號個人化飲料折扣情境

# ===== AI 使用與學習說明（使用 # 註解） =====
