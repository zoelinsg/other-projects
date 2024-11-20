# Python 銀行系統程式
# 參考來源：
# https://www.youtube.com/watch?v=8aW3tkIul-8&list=WL&index=22

def show_balance(balance):
    """
    顯示目前的帳戶餘額
    """
    print("*************************")
    # 使用 f-string 格式化顯示餘額
    print(f"您的帳戶餘額為：${balance:.2f}")  # 顯示到小數點後兩位
    print("*************************")

def deposit():
    """
    存款功能：讓用戶輸入存款金額，並檢查金額是否有效
    """
    print("*************************")
    # 輸入存款金額
    amount = float(input("請輸入存款金額："))
    print("*************************")
    
    if amount < 0:  # 檢查金額是否為負數
        print("*************************")
        print("金額無效，請重新輸入")
        print("*************************")
        return 0  # 返回 0 表示存款無效
    
    else:
        return amount  # 返回有效的存款金額

def withdraw(balance):
    """
    提款功能：讓用戶輸入提款金額，並檢查金額是否有效以及是否超過餘額
    """
    print("*************************")
    # 輸入提款金額
    amount = float(input("請輸入提款金額："))
    print("*************************")
    
    if amount > balance:  # 提款金額大於餘額
        print("*************************")
        print("餘額不足，請重新輸入")
        print("*************************")
        return 0  # 返回 0 表示提款失敗
    
    elif amount < 0:  # 檢查金額是否為負數
        print("*************************")
        print("金額必須大於 0")
        print("*************************")
        return 0  # 返回 0 表示提款失敗
    
    else:
        return amount  # 返回有效的提款金額

def main():
    """
    主功能：銀行系統的操作介面
    """
    balance = 0  # 初始餘額為 0
    is_running = True  # 用於控制程式是否繼續運行

    while is_running:
        print("*************************")
        print("      銀行管理系統       ")  # 程式名稱
        print("*************************")
        print("1. 顯示帳戶餘額")  # 顯示餘額
        print("2. 存款")          # 存款
        print("3. 提款")          # 提款
        print("4. 離開系統")      # 離開程式
        print("*************************")

        # 輸入使用者的選擇
        choice = input("請輸入選項 (1-4)：")
        if choice == '1':  # 選擇顯示餘額
            show_balance(balance)
        elif choice == '2':  # 選擇存款
            balance += deposit()  # 增加餘額
        elif choice == '3':  # 選擇提款
            balance -= withdraw(balance)  # 減少餘額
        elif choice == '4':  # 選擇退出
            is_running = False  # 停止迴圈，結束程式
        else:
            print("*************************")
            print("無效的選項，請重新輸入")  # 提示無效選項
            print("*************************")
    print("*************************")
    print("感謝您的使用，祝您有美好的一天！")  # 感謝訊息
    print("*************************")

if __name__ == "__main__":
    # 程式的執行入口
    main()
