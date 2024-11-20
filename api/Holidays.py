import requests  # 導入 requests 庫來發送 HTTP 請求

# API 基本 URL (使用 HTTPS)
base_url = "https://calendarific.com/api/v2/holidays"

# 定義函式來從 API 獲取假期數據
def get_holiday_data(api_key, country, year):
    url = f"{base_url}?api_key={api_key}&country={country}&year={year}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()  # 回傳 API 的 JSON 資料
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 錯誤: {http_err}")
    except Exception as err:
        print(f"其他錯誤: {err}")
    return None

# 定義函式來顯示假期資訊
def display_holiday_info(holiday_data):
    if holiday_data and 'response' in holiday_data and 'holidays' in holiday_data['response']:
        print("2025年的臺灣假日\n")
        for forecast in holiday_data['response']['holidays']:
            name = forecast['name']
            month = forecast['date']['datetime']['month']
            day = forecast['date']['datetime']['day']
            
            print(f"假日: {name}")
            print(f"日期: {month} 月 {day} 日")
            print("-" * 40)
    else:
        print("無法顯示數據，請檢查 API 回應是否包含 'holidays'.")

# API 金鑰和查詢條件
api_key = "UVTRVFu7zCbG7xSoxkKdsQYCKKN7BRwv"
country = "TW"
year = 2025

# 獲取假期數據並顯示結果
holiday_info = get_holiday_data(api_key, country, year)
display_holiday_info(holiday_info)
