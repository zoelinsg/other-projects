# 10/18免費方案以後暫停服務
import requests  # 導入 requests 庫來發送 HTTP 請求

# API 基本 URL
base_url = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather_data(lat, lon, api_key):
    """
    發送請求至 OpenWeatherMap API 並返回天氣數據.
    
    :param lat: 經度
    :param lon: 緯度
    :param api_key: API 金鑰
    :return: JSON 格式的天氣數據或 None (如有錯誤)
    """
    # 構建正確的 API 請求 URL
    url = f"{base_url}?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)  # 發送 GET 請求
        response.raise_for_status()  # 檢查請求是否成功
        return response.json()  # 解析回應的 JSON 數據
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 錯誤: {http_err}")  # 打印 HTTP 錯誤訊息
    except Exception as err:
        print(f"其他錯誤: {err}")  # 打印其他錯誤
    return None

def display_weather_info(weather_data):
    """
    打印天氣數據中的關鍵信息.
    
    :param weather_data: API 返回的天氣數據
    """
    if weather_data:
        print(f"總共有 {weather_data['cnt']} 條預測數據")
        for forecast in weather_data['list']:
            dt_txt = forecast['dt_txt']
            temp = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            print(f"時間: {dt_txt}, 溫度: {temp}°C, 天氣: {description}")
    else:
        print("無法顯示天氣數據，請檢查 API 回應.")

# 您的 API 金鑰
api_key = "ad09566d2f0f34027d4b7070d3d73240"
# 要查詢的地點經緯度
latitude = 23.5
longitude = 121

# 調用函數並獲取天氣數據
current_weather_info = get_weather_data(latitude, longitude, api_key)

# 顯示天氣信息
display_weather_info(current_weather_info)
