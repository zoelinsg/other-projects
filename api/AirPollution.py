import requests  # 導入 requests 庫來發送 HTTP 請求

# API 基本 URL (使用 HTTPS)
base_url = "https://api.openweathermap.org/data/2.5/air_pollution"

def get_air_pollution_data(lat, lon, api_key):
    """
    發送請求至 OpenWeatherMap API 並返回空氣污染數據.
    
    :param lat: 經度
    :param lon: 緯度
    :param api_key: API 金鑰
    :return: JSON 格式的空氣污染數據或 None (如有錯誤)
    """
    # 構建正確的 API 請求 URL
    url = f"{base_url}?lat={lat}&lon={lon}&appid={api_key}"
    try:
        response = requests.get(url)  # 發送 GET 請求
        response.raise_for_status()  # 檢查請求是否成功
        return response.json()  # 解析回應的 JSON 數據
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP 錯誤: {http_err}")  # 打印 HTTP 錯誤訊息
    except Exception as err:
        print(f"其他錯誤: {err}")  # 打印其他錯誤
    return None

def display_air_pollution_info(air_pollution_data):
    """
    顯示空氣污染數據.
    
    :param air_pollution_data: 從 API 返回的空氣污染數據
    """
    if air_pollution_data:
        # 遍歷數據列表中的每個預測
        for forecast in air_pollution_data['list']:
            co = forecast['components']['co']  # 一氧化碳
            no = forecast['components']['no']  # 氮氧化物 (一氧化氮)
            no2 = forecast['components']['no2']  # 二氧化氮
            o3 = forecast['components']['o3']  # 臭氧
            so2 = forecast['components']['so2']  # 二氧化硫
            pm2_5 = forecast['components']['pm2_5']  # PM2.5 懸浮微粒
            pm10 = forecast['components']['pm10']  # PM10 懸浮微粒
            nh3 = forecast['components']['nh3']  # 氨氣
            
            # 一列列顯示各個污染物的數值
            print("空氣污染數據:")
            print(f"一氧化碳 (CO): {co} μg/m3")
            print(f"一氧化氮 (NO): {no} μg/m3")
            print(f"二氧化氮 (NO2): {no2} μg/m3")
            print(f"臭氧 (O3): {o3} μg/m3")
            print(f"二氧化硫 (SO2): {so2} μg/m3")
            print(f"PM2.5 懸浮微粒: {pm2_5} μg/m3")
            print(f"PM10 懸浮微粒: {pm10} μg/m3")
            print(f"氨氣 (NH3): {nh3} μg/m3")
            print("-" * 40)  # 分隔線讓輸出更清晰
    else:
        print("無法顯示空氣污染數據，請檢查 API 回應.")

# 您的 API 金鑰
api_key = "ad09566d2f0f34027d4b7070d3d73240"
# 要查詢的地點經緯度
latitude = 23.5
longitude = 121

# 調用函數並獲取空氣污染數據
air_pollution_info = get_air_pollution_data(latitude, longitude, api_key)

# 顯示空氣污染信息
display_air_pollution_info(air_pollution_info)
