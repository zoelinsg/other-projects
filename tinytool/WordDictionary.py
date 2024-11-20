# Word Dictionary
# 引入 PyDictionary 模組，用於查詢單字的意思
from PyDictionary import PyDictionary

# 建立一個 PyDictionary 物件，用來查詢單字的意思
dictionary = PyDictionary()

# 使用無限迴圈來持續讓使用者輸入單字
while True:
    # 提示使用者輸入單字
    word = input("Enter your word: ")  # 讓使用者輸入單字
    
    # 如果使用者沒有輸入內容，則結束程式
    if word == "":
        break  # 當輸入為空字串時，跳出迴圈
    
    # 查詢並顯示單字的意思
    meaning = dictionary.meaning(word)  # 查詢單字的意思
    
    # 檢查是否有查詢結果，如果沒有，提示單字未找到
    if meaning:
        print(meaning)  # 如果找到單字意思，則顯示
    else:
        print(f"No meaning found for '{word}'.")  # 如果沒有找到意思，顯示錯誤訊息

