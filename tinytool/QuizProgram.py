# Quiz Program
# 小測驗程式
quiz = {
    "question1": {
        "question": "What is the capital of France?",  # 問題：法國的首都是哪裡？
        "answer": "Paris"  # 答案：巴黎
    },
    "question2": {
        "question": "What is the capital of Germany?",  # 問題：德國的首都是哪裡？
        "answer": "Berlin"  # 答案：柏林
    },
    "question3": {
        "question": "What is the capital of Italy?",  # 問題：義大利的首都是哪裡？
        "answer": "Rome"  # 答案：羅馬
    },
    "question4": {
        "question": "What is the capital of Spain?",  # 問題：西班牙的首都是哪裡？
        "answer": "Madrid"  # 答案：馬德里
    },
    "question5": {
        "question": "What is the capital of Portugal?",  # 問題：葡萄牙的首都是哪裡？
        "answer": "Lisbon"  # 答案：里斯本
    },
    "question6": {
        "question": "What is the capital of Switzerland?",  # 問題：瑞士的首都是哪裡？
        "answer": "Bern"  # 答案：伯恩
    },
    "question7": {
        "question": "What is the capital of Austria?",  # 問題：奧地利的首都是哪裡？
        "answer": "Vienna"  # 答案：維也納
    },
}

# 初始化得分變數
score = 0

# 迴圈遍歷每個問題與答案
for key, value in quiz.items():
    # 印出問題
    print(value['question'])  # 修正 'question' 的索引鍵，去掉多餘空格
    answer = input("Answer? ")  # 從使用者那裡獲取答案

    # 比較使用者的答案（忽略大小寫）是否正確
    if answer.lower() == value['answer'].lower():  # 修正 'answer' 的索引鍵，去掉多餘空格
        print('Correct')  # 如果答案正確，印出 "Correct"
        score += 1  # 得分增加 1
        print("Your score is: " + str(score))  # 印出目前得分
        print("\n")  # 印出兩行空白以分隔問題
    else:
        print("Wrong!")  # 如果答案錯誤，印出 "Wrong!"
        print("The answer is: " + value['answer'])  # 提示正確答案
        print("Your score is: " + str(score))  # 印出目前得分
        print("\n")  # 印出兩行空白以分隔問題

# 完成測驗後，顯示總得分與正確率
print("You got " + str(score) + " out of 7 questions correctly")  # 顯示正確回答的題數
print("Your percentage is " + str(int(score / 7 * 100)) + "%")  # 顯示正確率百分比
