# 拉麵點餐系統
print("歡迎使用拉麵點餐機~")
print("(1)鹽味拉麵$220")
print("(2)醬油拉麵$240")
print("(3)豚骨拉麵$280")

soup=input("請選擇拉麵口味(輸入:1 or 2 or 3)")
big=input("是否加大,豚骨口味+$50其他口味+$38(輸入:Yor N)")
egg=input("是否加糖心蛋+$30(輸入:Y or N)")
pork=input("是否加叉燒+$60(輸入:Y or N)")

bill = 0

if soup == "1":
    bill += 220
elif soup == "2":
    bill += 240
elif soup == "3":
    bill += 280

if big == "Y":
    if soup == "3":
        bill += 50
    else:
        bill += 30

if egg == "Y" :
    bill += 30

if pork == "Y":
    bill += 60

if big == "Y" and egg == "Y" and pork == "Y":
    bill += 20
    print(f"加好加滿折價$20, 總金額${bill},感謝您的光臨!")
else:
    print(f"總金額${bill}, 感謝您的光臨!")